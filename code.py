class DataValidator:
    def validate_inputs(self, input_list):
      
        if not isinstance(input_list, list):
            raise ValueError("Input must be a list")
        if not all(isinstance(item, str) for item in input_list):
            raise ValueError("All items in the list must be strings")

        valid_integers = []

  
        for item in input_list:
            if item.isdigit():
                valid_integers.append(int(item))


        assert all(isinstance(item, int) and item > 0 for item in valid_integers), "List contains only positive integers"
        assert len(valid_integers) <= len(input_list), "New list is not longer than the input list"

        return valid_integers


