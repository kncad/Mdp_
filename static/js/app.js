document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', () => {
        const row = button.getAttribute('data-row');
        const col = button.getAttribute('data-col');

        // Send player's move to the server
        fetch('/move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                player: 1, // Human player
                action: [parseInt(row), parseInt(col)]
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.result) {
                document.getElementById('result').innerText = data.result;
            } else {
                // Update AI move on the board
                const [aiRow, aiCol] = data.ai_move;
                document.querySelector(`button[data-row='${aiRow}'][data-col='${aiCol}']`).innerText = 'O';
            }
        });
        
        button.innerText = 'X';  // Mark player's move
        button.disabled = true;   // Disable the button after the move
    });
});
