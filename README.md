# InvestMentor  

**InvestMentor** is a Django-based web application that helps users make smarter investment decisions.  
It provides three main tools:  

1. **Investment Planner** – Generate personalized investment allocations based on experience level and monthly savings.  
2. **Broker Comparison Tool** – Compare Indian stock brokers across fees, reviews, UI, and support.  
3. **AI-Powered Learning Roadmap** – Uses **LLaMA 2 via Ollama** to create customized investment learning roadmaps based on current and target knowledge levels.  

---

## Features
- Modern **TailwindCSS UI** with responsive design.  
- Interactive charts for investment allocation (Chart.js).  
- Dynamic broker comparison with scoring system.  
- AI integration with **LLaMA 2** to generate structured learning plans.  

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)  
- **Frontend:** HTML, TailwindCSS, Chart.js, Vanilla JS  
- **AI Integration:** LLaMA 2 via [Ollama](https://ollama.ai/)  
- **Database:** SQLite (default, can be switched to PostgreSQL/MySQL)  

---

## Installation & Setup  
1. Clone the repo  
	```bash  
    git clone https://github.com/<your-username>/InvestMentor.git  
    cd InvestMentor

2. Setup virtual environment  
    ```bash
	python -m venv venv # On Windows  
	source venv/bin/activate # On Mac/Linux  

3. Install dependencies  
    ```bash
	pip install Django  
	pip install requests
	pip install chartjs

4. Run database migrations  
    ```bash
	python manage.py migrate  

5. Start Django server 
    ```bash
	python manage.py runserver   
	Now visit http://127.0.0.1:8000/

## LLaMA 2 Integration (via Ollama)
The AI Roadmap Generator depends on Ollama to run LLaMA locally.

1. Install Ollama
- Download and install from Ollama.ai
- Verify installation:  
    ```bash
	ollama --version

2. Pull the LLaMA 2 model
    ```bash
	ollama pull llama2

3. Run Ollama server
- In a separate terminal (before using roadmap): 
    ```bash
	ollama run llama2

## License
This project is open-source under the MIT License.
