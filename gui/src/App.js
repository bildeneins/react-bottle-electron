import './App.css';
import axios from "axios"

function App() {
    function onClicked_get() {
        console.log("send get request")
        axios.get("http://localhost:8080/get",{
            headers: {
                "Content-Type": "application/json",
                'Access-Control-Allow-Origin': "http://localhost:8080/",
            }
        })
            .then(function (res) {
                console.log("got get response")
                alert(res.data)
        })
            .catch(error => {
            console.log(error);
        });
    }
    function onClicked_post() {
        console.log("send post request")
        axios.post("http://localhost:8080/post", "post data",{
            headers: {
                "Content-Type": "application/json",
                'Access-Control-Allow-Origin': "http://localhost:8080/",
            }
        })
            .then(function (res) {
                console.log("got post response")
                alert(res.data)
            })
            .catch(error => {
                console.log(error);
            });
    }
  return (
    <div className="App">
      <div className="App-img">
          <h1>daaaaa</h1>
          <button onClick={onClicked_get}>
              get request button
          </button>
          <button onClick={onClicked_post}>
              post request button
          </button>
          {/*<img src="http://localhost:8080/video_feed"  width="900" height="500"/>*/}
      </div>
    </div>
  );
}

export default App;

