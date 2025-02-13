# dm-lab-home-assignment

## Project overview

This project collects **biker traffic data** from **Eco-Counter's** three monitoring stations located in Budapest (Bem tér, Hungária körút and Árpád-híd). It stores the collected data in a postgresql database, processes the data which is available via an API or the Frontend. 

I got the idea for this project as i was passig one of these measuring points and I was interested in seeing the trends in bike traffic. I was expecting a growing trend in traffic over the years, which was not the case, but this might actually be because there are a growing number of bike lanes in the city and the traffic to spread out more. 

## Used technologies
- **Backend:** FastAPI, Python, Pandas  
- **Frontend:** Vue, TypeScript, Vite, Vuetify  
- **Database:** PostgreSQL  
- **Containerization:** Docker  
- **IDE:** VSCode (WSL)  

## Architecture
### Microservices

- **Frontend:** Displays processed data  
- **Backend:** Retrieves data from the database, processes data, and serves it via API endpoints  
- **Dataloader:** Creates the database, fetches data from the external API, and loads it into the database  


## Steps to run
1. Clone the repository
2. Run microservices: docker-compose up --build
3. Access services:
    - API: http://localhost:8000/docs
    - Frontend: http://localhost:5173/
    - Database: http://localhost:5050/


### **Deployment Plan (Not Implemented)**  
Currently, this project runs locally using Docker Compose. For deployment, the following setup could be used:  

- **Google Cloud Platform** as the cloud provider.  
- **Google Kubernetes Engine** to manage the microservices  
- **Google Cloud Storage & Secret Manager** for storing data and credentials  
- **GitHub Actions** for automating deployment  

Each microservice stored in Google’s container registry as a Docker container. A **Kubernetes cluster** runs these services and handles scaling. The **frontend and API** would be accessible via a public URL.
