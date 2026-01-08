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

def annotate_variable_importance(graph):
    for node in graph.nodes:
        # 1. Access the esl_info where the parser stores comments
        esl_info = node.annotations.get("esl_info", {})
        tagged_comments = esl_info.get("tagged_comments", {})
        print(tagged_comments)
        # 2. Check for the specific tag key "@importance"
        # Note: RaGraph parsers typically strip the '@' for the dict key, 
        # so check 'importance'.
        if "importance" in tagged_comments:
            # Tags are usually stored as a list of strings
            values = tagged_comments["importance"]
            
            if values:
                # 3. Parse the string value ("true"/"false") to a boolean
                # We take the first value found
                raw_value = str(values[0]).strip().lower()
                is_important = raw_value == "true"
                
                # 4. Set the actual annotation on the node object
                node.annotations["importance"] = is_important
                
                # Optional: Print for verification
                # print(f"Annotated '{node.name}' as importance={is_important}")
            else:
                # Handle empty tag (e.g. just "#< @importance")
                # Defaulting to True if the tag is present but empty
                node.annotations["importance"] = True