from flask import Flask, request, jsonify
from flask_cors import CORS   # 추가!

app = Flask(__name__)
CORS(app)  # 모든 origin 허용 (테스트/발표용 안전!)

current_emotion = None

@app.route('/trigger', methods=['POST'])
def update_emotion():
    try:
        data = request.get_json(force=True)
        emotion = data.get("emotion")
        if emotion not in ["SLEEPY", "RELAXED", "STRESSED"]:
            return jsonify({"error": "Invalid emotion type"}), 400
        global current_emotion
        current_emotion = emotion
        print(f"💡 감정 수신됨: {emotion}")
        return jsonify({"status": f"{emotion} received"}), 200
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return jsonify({"error": "Invalid request", "detail": str(e)}), 400

@app.route('/emotion', methods=['GET'])
def get_emotion():
    global current_emotion
    if current_emotion is None:
        return "NONE", 200
    return current_emotion, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

