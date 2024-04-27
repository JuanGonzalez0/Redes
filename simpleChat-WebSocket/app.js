//importo webSocket y creo el server
const webSocket = require('ws')
const server = new webSocket.Server({port:'8080'})

const welcomeMessage = "¡Bienvenido al chat!";

//server prendido y esperando que un cliente se conecte
server.on('connection', socket => {

    console.log('Client connected')
    socket.send(welcomeMessage);

    server.clients.forEach(client => {
        if (client !== socket && client.readyState === webSocket.OPEN) {
            client.send("¡Un nuevo usuario se ha unido al chat!");
        }
    }); //avisa de que un nuevo cliente ingreso al chat

    socket.on('message', message => { //recibe el mensaje del cliente
        server.clients.forEach(client=>{ //revisa si el cliente sigue conectado
            if(client.readyState === webSocket.OPEN)
                client.send(`${message}`)
        })
    })
})

console.log('socket initialized on port 8080')
