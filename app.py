from flask import Flask, request, jsonify
import sqlite3
from typing import List

app = Flask(__name__)

def isValid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == num:
                return False
    return True

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for num in range(1, 10):
                    if isValid(board, i, j, str(num)):
                        board[i][j] = str(num)
                        if solve(board):
                            return True
                        board[i][j] = '.'
                return False
    return True

def save_player_record(name, score, errors, moves):
    conn = sqlite3.connect('sudoku_game.db')
    c = conn.cursor()

    # Insert a new player record
    c.execute('''
        INSERT INTO players (name, score, errors, moves)
        VALUES (?, ?, ?, ?)
    ''', (name, score, errors, moves))

    conn.commit()
    conn.close()

@app.route("/solve_sudoku", methods=["POST"])
def solve_sudoku():
    board = request.json.get("board")
    name = request.json.get("name")
    score = request.json.get("score")
    errors = request.json.get("errors")
    moves = request.json.get("moves")

    if solve(board):
        save_player_record(name, score, errors, moves)
        return jsonify({"status": "success", "board": board}), 200
    else:
        return jsonify({"status": "failure", "message": "No solution found"}), 400

if __name__ == "__main__":
    app.run(debug=True)
