import { useState } from "react";
import "./App.css"; // Import the CSS file

const ROWS = 6;
const COLS = 7;

export default function App() {
  const [board, setBoard] = useState(
    Array(ROWS)
      .fill(null)
      .map(() => Array(COLS).fill(0))
  );

  const [currentPlayer, setCurrentPlayer] = useState(1);
  const [gameOver, setGameOver] = useState(false);
  const [message, setMessage] = useState("");

  const handleClick = async (col) => {
    if (gameOver) return;
    try {
      const response = await fetch("https://connectfour-fiis.onrender.com/move", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          board,
          player: currentPlayer,
          column: col,
        }),
      });
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();
      console.log("Response from backend:", data);

      const { new_board, winner, draw } = data;
      setBoard(new_board);

      if (winner !== 0) {
        setMessage(`Player ${winner} wins!`);
        setGameOver(true);
      } else if (draw) {
        setMessage("It's a draw!");
        setGameOver(true);
      } else {
        setCurrentPlayer((prev) => (prev === 1 ? 2 : 1));
      }
    } catch (err) {
      console.error("Error during move:", err);
    }
  };

  return (
    <div className="app-container">
      <h1 className="title">Connect Four</h1>
      <div className="board">
        {board.map((row, rowIndex) =>
          row.map((cell, colIndex) => (
            <div
              key={`${rowIndex}-${colIndex}`}
              onClick={() => handleClick(colIndex)}
              className="cell"
            >
              <div
                className={`disk ${
                  cell === 1 ? "disk-red" : cell === 2 ? "disk-yellow" : ""
                }`}
              ></div>
            </div>
          ))
        )}
      </div>
      {message && <p className="message">{message}</p>}
    </div>
  );
}
