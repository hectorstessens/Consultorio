import express, { Application } from 'express';
import morgan from 'morgan';
import cors from 'cors';

import indexRoutes  from './routes/indexRoutes';
import { Routes } from './routes/routes';
import { PacienteController } from './controller/pacienteController';
import { PersonaController } from './controller/personaController';

class Server {
    public app: Application;
    constructor() {
        this.app = express();
        this.config();
        this.routes();
    }

    config(): void {
        this.app.set('port', process.env.PORT || 3000);

        this.app.use(morgan('dev'));
        this.app.use(cors());
        this.app.use(express.json());
        this.app.use(express.urlencoded({extended: false}));
    }
    
    routes(): void 
    {
        this.app.use(indexRoutes);
        const route = new Routes();
        this.app.use('/api/persona', route.route(new PersonaController()));    
        this.app.use('/api/paciente', route.route(new PacienteController()));
     }

    start(): void {
        this.app.listen(this.app.get('port'), () => {
            console.log('server on port',this.app.get('port'));
        });
    }
}
const server = new Server();
server.start();