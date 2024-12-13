
let board = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.']
];


function createBoard() {
    const table = document.getElementById('board');
    table.innerHTML = '';
    
    for (let i = 0; i < 9; i++) {
        let row = document.createElement('tr');
        for (let j = 0; j < 9; j++) {
            let cell = document.createElement('td');
            let input = document.createElement('input');
            input.type = 'text';
            input.maxLength = 1;
            input.value = board[i][j] === '.' ? '' : board[i][j];
            input.id = `cell-${i}-${j}`;
            input.addEventListener('input', (e) => handleInputChange(i, j, e));
            cell.appendChild(input);
            row.appendChild(cell);
        }
        table.appendChild(row);
    }
}


function handleInputChange(i, j, e) {
    const value = e.target.value;
    if (value === '' || /^[1-9]$/.test(value)) {
        board[i][j] = value;
    } else {
        e.target.value = board[i][j];
    }
}


function solveSudoku() {
    if (solve(board)) {
        renderBoard();
    } else {
        alert('No solution found!');
    }
}


function solve(board) {
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            if (board[i][j] === '.') {
                for (let num = 1; num <= 9; num++) {
                    const numStr = num.toString();
                    if (isValid(board, i, j, numStr)) {
                        board[i][j] = numStr;
                        if (solve(board)) {
                            return true;
                        }
                        board[i][j] = '.';  
                    }
                }
                return false;  
            }
        }
    }
    return true;  
}

function isValid(board, row, col, num) {
   
    for (let i = 0; i < 9; i++) {
        if (board[row][i] === num || board[i][col] === num) {
            return false;
        }
    }

    
    const startRow = Math.floor(row / 3) * 3;
    const startCol = Math.floor(col / 3) * 3;
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (board[startRow + i][startCol + j] === num) {
                return false;
            }
        }
    }

    return true;
}

function renderBoard() {
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const input = document.getElementById(`cell-${i}-${j}`);
            input.value = board[i][j] === '.' ? '' : board[i][j];
        }
    }
}


function clearBoard() {
    board = board.map(row => row.map(() => '.'));
    renderBoard();
}

window.onload = createBoard;
