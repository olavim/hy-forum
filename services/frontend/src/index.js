import path from 'path';
import dotenv from 'dotenv';
import app from './app';

dotenv.config({path: path.resolve(__dirname, '../.env')});

const server = app();

const port = parseInt(process.env.PORT || '5001', 10);
server.listen(port, () => {
	console.log(`Server listening on port: ${port}`);
});
