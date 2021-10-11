import './App.css';
import axios from "axios"

function App() {
    function handleClick() {
        axios.get("http://localhost:8080/")
            .then(function (res) {
                console.log(res.data)
        })
            .catch(error => {
            console.log(error);
        });
    }
    return (
    <div className="App">
      <div className="App-img">
          <h1>Bottle Streaming Sample</h1>
          <button onClick={handleClick}>
              GET while streaming
          </button>
          <img src="http://localhost:8080/video_feed" alt="video" width="900" height="500"/>
      </div>
    </div>
    );
}

export default App;

