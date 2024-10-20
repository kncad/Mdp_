let currentPlayer = 1;  // 1 for player, -1 for AI

function handlePlayerMove(x, y) {
    if (currentPlayer !== 1 || board[x][y] !== 0) {
        return;
    }
    
    // Update the board and send the move to the server
    updateBoard(x, y, 1);
    currentPlayer = -1;  // Switch to AI turn

    // Call AI to make its move
    makeAiMove();
}

function makeAiMove() {
    fetch('/ai_move', {
        method: 'POST',
        body: JSON.stringify(board),  // Send current board to the server
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        updateBoard(data.x, data.y, -1);  // Update board with AI's move
        currentPlayer = 1;  // Switch back to player turn
        checkForWinner();
    });
}

function checkForWinner() {
    // Check if either the player or AI has won or if the game is a draw
    let winner = getWinner();
    if (winner) {
        displayWinner(winner);
        showNewGameButton();  // Option to reset the game
    }
}
