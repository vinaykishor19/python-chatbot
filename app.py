from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').lower()

    # Responses based on user intent
    if "python project" in user_message or "freelancer" in user_message:
        response = "Absolutely! I’m a freelance Python developer with experience in automation, web scraping, and data analysis. Could you tell me more about your project?"
    elif "automate" in user_message or "scraper" in user_message or "web scraping" in user_message:
        response = "I can build a scraper using BeautifulSoup, Selenium, or Scrapy. I can also export the data to Excel, CSV, or a database. Do you have a target website or format in mind?"
    elif "timeline" in user_message or "how long" in user_message or "delivery" in user_message:
        response = "Typically, small scripts are delivered within 1-3 days. Larger data analysis tasks may take 4-7 days. Share your requirements for a precise estimate."
    elif "cost" in user_message or "price" in user_message or "charges" in user_message:
        response = "Simple scripts usually start at $50. For larger projects, I’ll give a detailed quote after understanding the scope and timeline."
    elif "how do you work" in user_message or "process" in user_message:
        response = "I follow a step-by-step process: understand your needs, provide a timeline & quote, develop in stages, share updates, and deliver well-documented code."
    elif "can you help" in user_message or "help" in user_message:
        response = "Of course! I can help with Python development, data analysis, and automation tasks. Let me know what you’re working on."
    elif "hi" in user_message or "hello" in user_message or "hey" in user_message:
        response = "Hi there! I'm Vinay, a freelance Python developer. I help clients automate tasks, analyze data, and build tools. How can I assist you today?"
    elif "thank you" in user_message or "thanks" in user_message:
        response = "You're welcome! I'm here whenever you're ready to discuss your project further."
    elif "bye" in user_message or "goodbye" in user_message:
        response = "Goodbye! Looking forward to collaborating with you soon."
    elif "experience" in user_message:
        response = "I have several years of experience working with clients globally on Python, data scraping, Excel automation, and data analytics using pandas, NumPy, and more."
    elif "skills" in user_message or "what do you know" in user_message:
        response = "I’m skilled in Python, pandas, NumPy, Selenium, BeautifulSoup, Flask, APIs, Excel automation, data visualization, and more."
    elif "about you" in user_message or "who are you" in user_message:
        response = "I'm Vinay, a freelance Python developer and data analyst. I build efficient, scalable solutions for automation, scraping, and analysis. I also ensure clean and maintainable code."
    elif "how to contact" in user_message or "contact" in user_message:
        response = "You can reach me via email or directly through the platform you're contacting me on. I respond quickly and value clear communication."
    elif "portfolio" in user_message or "previous work" in user_message:
        response = "I've worked on data dashboards, Python scrapers, Excel automation, and more. I’d be happy to share code samples or case studies upon request."
    elif "payment" in user_message or "pay" in user_message:
        response = "I accept payments via Upwork, Fiverr, Payoneer, or bank transfer. We can always discuss what's convenient for you."
    elif "working hours" in user_message or "timezone" in user_message:
        response = "I'm based in India (IST) and usually work flexible hours to accommodate clients globally."
    else:
        response = "I'm here to assist you with Python development, data automation, and analysis tasks. Could you provide a bit more detail on what you need?"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
