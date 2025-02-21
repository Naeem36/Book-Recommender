function sendData() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("output").innerHTML = this.responseText;
        }
    };
    xhr.open("POST", "/recommend", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({string: document.getElementById("title").value}));
}

xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        document.getElementById("output").innerHTML = this.responseText;
    }
};