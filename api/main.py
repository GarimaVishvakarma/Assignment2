from flask import Flask, jsonify, request
from utils import Solution
import multiprocessing as mp

app = Flask(__name__)


@app.route('/solution/<int:n>', methods=['GET'])
def home(n):
    f = open(r"../input.txt", "r", encoding="utf-8")
    nums = f.readlines()
    work = []
    sol = Solution(nums, n)
    try:
        p1 = mp.Process(target=sol.multiply_data)
        p2 = mp.Process(target=sol.add_data)
        work.append(p1)
        work.append(p2)
        p1.start()
        p2.start()
        for x in work:
            x.join()
        return jsonify({'data': "success"})
    except Exception as e:
        return jsonify({'error': e})


if __name__ == '__main__':
    app.run(host="localhost", debug=True)