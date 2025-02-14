const wsScheme = window.location.protocol === "https:" ? "wss" : "ws";
const socket = new WebSocket(`${wsScheme}://${window.location.host}/ws/online-status/`);

socket.onopen = function () {
    console.log("WebSocket conectado!");
};

socket.onerror = function (error) {
    console.error("Erro no WebSocket:", error);
};

socket.onclose = function () {
    console.log("WebSocket desconectado!");
};
