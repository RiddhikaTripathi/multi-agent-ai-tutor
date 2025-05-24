# 🤖 Multi-Agent AI Tutor

A multi-agent tutoring system built using FastAPI and Google Gemini API, deployed on Railway. The project follows Google's Agent Development Kit (ADK) principles to intelligently delegate user queries across subject-specific agents: Math, Physics, and Chemistry.

---

## 📌 Live Demo

🚀 **Try it now**:  
👉 [https://multiagentaitutor-production.up.railway.app/docs](https://multiagentaitutor-production.up.railway.app/docs)  
Use the `/ask` endpoint to interact with the Tutor Agent.

Example request:
```json
{
  "query": "Can you help me solve 2x + 5 = 11?"
}
```
---

## 🧠 How It Works

Tutor Agent: Handles incoming user queries and routes them to the appropriate subject expert agent using Gemini-powered intent recognition.

Math Agent: Solves algebraic and arithmetic problems. Uses a custom calculator tool for basic arithmetic.

Physics Agent: Answers physics-related questions. Uses a constants lookup tool.

Chemistry Agent: Handles chemistry-related queries, such as chemical formulas and reactions.

---

## ⚙️ Project Structure

```
multi-agent-ai-tutor/
├── agents/
│   ├── gemini.py            # Gemini API helper
│   ├── math_agent.py        # Math Agent with calculator tool
│   ├── physics_agent.py     # Physics Agent with constants lookup
│   ├── chemistry_agent.py   # Chemistry Agent
│   └── tutor_agent.py       # Routes queries to the correct agent
├── main.py                  # FastAPI app entry point
├── requirements.txt         # Dependencies
├── .env                     # API key file (not tracked)
└── README.md                # Project documentation
```

---

## 🛠️ Technologies Used

| Tech        | Purpose                                      |
|-------------|----------------------------------------------|
| Python      | Core programming language                    |
| FastAPI     | Web API framework                            |
| Gemini API  | LLM for language understanding and replies   |
| Railway     | Deployment platform                          |
| GitHub      | Version control and collaboration            |

---

## 🔐 Environment Setup

### Clone the repo
```bash
git clone https://github.com/RiddhikaTripathi/multi-agent-ai-tutor.git
cd multi-agent-ai-tutor
```
### Create a .env file
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Run locally
```bash
uvicorn main:app --reload
```
Visit: http://localhost:8000/docs to try the API.

---

## ✅ Features

- **Tutor Agent** uses Gemini to identify the subject of a question  
- Each **sub-agent** can independently handle tasks in its domain  
- **Math Agent** includes a simple arithmetic calculator  
- **Physics Agent** includes a scientific constant lookup  
- **Chemistry Agent** handles chemical queries  
- Deployed with a public `/ask` API endpoint  

---

## 🧪 Sample Queries

| Query                                 | Routed To       |
|---------------------------------------|-----------------|
| "Can you solve 5 + 3 * 2?"            | Math Agent      |
| "What is Newton's second law?"        | Physics Agent   |
| "What is the chemical formula of water?" | Chemistry Agent |

---

## 🛫 Deployment

- Deployed on **Railway**
- Environment variable set as `GEMINI_API_KEY`
- Public API docs available at:  
  🔗 [https://multiagentaitutor-production.up.railway.app/docs](https://multiagentaitutor-production.up.railway.app/docs)

---

## 🙋‍♀️ Author

**Built by:** Riddhika Tripathi  
