# This file implement evaluations.
import Individual as id


def execution(creator, program, data):
    '''
    This function execute a program over the data, and returns the status of output register for each data entry
    Parameteres:
        creater: contain the unvisal rules govering all programs
        program: is the array of programs
        data: is a set of data entries
    Returns:
        status of output registers for all entries
    '''
    # ---- program initialzation ----
    program_code = id.compile_program(program)
    # ---- execute program for all entries ----
    m = data.values
    res = [run(creator.arr_registers_output, creator.arr_registers_arithmatic, creator.arr_registers_var, program_code, m[i]) for i in range(len(m))]
    return res

def run(arr_r_o, arr_r_a, arr_r_f, code, arr_feature):
    # initialize value
    arr_name = arr_r_o
    arr_val = [0]*len(arr_name)
    arr_name = arr_name + arr_r_a
    arr_val = arr_val + [0]*len(arr_r_a)
    arr_name = arr_name + arr_r_f
    arr_val = arr_val + [v for v in arr_feature]
    dic = dict(zip(arr_name, arr_val))
    # run program
    exec(code,dic)
    return [dic[v] for v in arr_r_o]
        
    