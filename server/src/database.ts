import mysql from 'promise-mysql';
import keys from './keys';

const pool = mysql.createPool(keys.database);

pool.get('getConnection')
    .then(connection => {
        pool.return(connection);
        console.log('DB is Connected');
    });

export default pool;
