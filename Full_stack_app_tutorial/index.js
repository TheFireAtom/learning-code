const express = require('express');

const app = express();

const { readFile } = require('fs');

app.get('/', (request, responce) => {
    readFile('./some.html', 'utf8', (err, html) => {
     
        if (err) {
            responce.status(500).send('server error');
        }

        responce.send(html);
    });
});

app.listen(process.env.PORT || 3000, () => console.log('App is available on http://localhost:3000'));