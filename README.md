# AI Product Recommender

A full-stack application that allows users to search for products using natural language. It uses the **Google Gemini API** to understand user queries, extract filters (like category, brand, maximum price), and then queries **MongoDB** to find matching products.

## Tech Stack
- **Frontend:** React, TypeScript, Vite
- **Backend:** FastAPI, Python, Motor (Async MongoDB Driver)
- **Database:** MongoDB Atlas
- **AI Integration:** Google Gemini API

## Project Structure
- `/frontend`: Contains the React/Vite application.
- `/backend`: Contains the FastAPI backend and AI logic.

---

## How to Run Locally

### 1. Prerequisites
- [Node.js](https://nodejs.org/) installed
- [Python 3.9+](https://www.python.org/) installed
- A MongoDB Atlas account/database
- A Google Gemini API Key

### 2. Backend Setup
1. Open a terminal and navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the `backend` directory with your credentials:
   ```env
   MONGODB_URI=mongodb+srv://<your_user>:<your_password>@cluster0...
   MONGODB_DB=spearmint
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
5. Run the FastAPI server:
   ```bash
   uvicorn app:app --reload --port 8000
   ```
   *The API will be available at `http://localhost:8000`*

### 3. Frontend Setup
1. Open a **new** terminal and navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install the dependencies:
   ```bash
   npm install
   ```
3. (Optional) Create a `.env` file in the `frontend` directory to specify the backend URL (it defaults to `http://localhost:8000/api` if omitted):
   ```env
   VITE_API_URL=http://localhost:8000/api
   ```
4. Start the Vite development server:
   ```bash
   npm run dev
   ```
   *The web application will be available at `http://localhost:5173`*

---

## Deployment
- **Backend:** Designed to be easily deployed on [Render](https://render.com/). Just set the Root Directory to `backend` and use `uvicorn app:app --host 0.0.0.0 --port 10000` as the start command.
- **Frontend:** Designed to be easily deployed on [Vercel](https://vercel.com/). Vercel will automatically detect the Vite preset. Make sure to set the `VITE_API_URL` environment variable to your deployed backend URL.
