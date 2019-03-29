    with open('data_an_x' + str(order) + '.txt','a+') as data_an_x_f,open('data_an_y' + str(order) + '.txt','a+') as data_an_y_f,open('data_an_z' + str(order) + '.txt','a+') as data_an_z_f:
        for data_an_index in ran_data_an:
            data_an_keys = data_an_index.keys()
            for data_an_keys_index in data_an_keys:
                if data_an_keys_index == "ran_data_an_x":
                    data_an_x_f.write(str(data_an_index[data_an_keys_index]) + " ")
                elif data_an_keys_index == "ran_data_an_y":
                    data_an_y_f.write(str(data_an_index[data_an_keys_index]) + " ")
                elif data_an_keys_index == "ran_data_an_z":
                    data_an_y_f.write(str(data_an_index[data_an_keys_index]) + " ")