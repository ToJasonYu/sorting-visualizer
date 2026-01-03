from flask import Flask, jsonify, request
from flask_cors import CORS
import sorting_algorithms

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import sorting_algorithms

app = Flask(__name__)
CORS(app) 

@app.route('/sort', methods=['POST'])
def sort_array():
    data = request.json
    array = data.get('array')
    algorithm = data.get('algorithm')

    if not array or not algorithm:
        return jsonify({"error": "Missing array or algorithm"}), 400

    algos = {
        "bubble": sorting_algorithms.bubble_sort,
        "selection": sorting_algorithms.selection_sort,
        "insertion": sorting_algorithms.insertion_sort,
        "quick": lambda arr: sorting_algorithms.quick_sort(arr, 0, len(arr)-1),
        "merge": lambda arr: sorting_algorithms.merge_sort(arr, 0, len(arr)-1),
        "heap": sorting_algorithms.heap_sort,
        "shell": sorting_algorithms.shell_sort,
        "cocktail": sorting_algorithms.cocktail_shaker_sort,
        "gnome": sorting_algorithms.gnome_sort,
        "radix": sorting_algorithms.radix_sort
    }

    if algorithm not in algos:
        return jsonify({"error": "Algorithm not supported"}), 400

    steps = []
    arr_copy = array.copy()
    
    for step_result in algos[algorithm](arr_copy):
        if len(step_result) == 3:
            arr_state, locked_state, active_state = step_result
        else:
            arr_state, locked_state = step_result
            active_state = []

        steps.append({
            "array": list(arr_state),
            "locked": locked_state,
            "active": active_state
        })

    return jsonify({"steps": steps})

#if __name__ == '__main__':
#    app.run(debug=True, host='0.0.0.0')