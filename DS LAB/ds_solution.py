def manipulate_data(data_type=None, data=None):
    accepted_data_types = {
        'list': 'data[-1:: -1]',
        'set': 'set.union(data, ["ANDELA", "TIA", "AFRICA"])',
        'dictionary': '[keys for keys, item in data.items()]'
    }
    try:
        return eval(accepted_data_types['%s' % data_type])
    except KeyError as e:
        print("\nYou failed to pass the correct data type.\n%s\n" % e)