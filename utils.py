# Function to set the weights
def set_edge_weights(graph):
    for e in graph.edges:
        for func in (
            e.annotations.get("esl_info", {})
            .get("reason", {})
            .get("relation_specifications", [])
        ):
            esl_info = graph[func].annotations.get("esl_info", {})
            required_vars = esl_info.get("required_variables", [])
            
            if e.source.name not in required_vars:
                index = 0
            else:
                index = required_vars.index(e.source.name)

            for weight in ["weight"]:
                weights = esl_info.get("tagged_comments", {}).get(weight, [1.0])

                if len(weights) <= index:
                    weight_value = 1.0
                else:
                    weight_value = float(weights[index])
                
                e.weights[weight] = weight_value
