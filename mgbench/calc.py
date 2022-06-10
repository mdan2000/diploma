def get_avr(l):
    return sum(l) / len(l)

def calc_halfduplex():
    filename = 'l1-halfduplex.log'
    with open(filename, 'r') as r:
        lines = [line for line in r]
        from_host_to_gpu = lines[6:10].copy()
        from_gpu_to_host = [lines[10], lines[14], lines[18], lines[22]]
        from_gpu_to_gpu = lines[11:14].copy() + lines[15:18].copy() + lines[19:22].copy() + lines[23:26].copy()

    speed_from_host_to_gpu = get_avr([float(res.split()[6]) for res in from_host_to_gpu])
    speed_from_gpu_to_host = get_avr([float(res.split()[6]) for res in from_gpu_to_host])
    speed_from_gpu_to_gpu = get_avr([float(res.split()[7]) for res in from_gpu_to_gpu])
    print('Test halfduplex')
    print(f'AVR speef from host to gpu: {speed_from_host_to_gpu}')
    print(f'AVR speef from gpu to host: {speed_from_gpu_to_host}')
    print(f'AVR speef from gpu to gpu: {speed_from_gpu_to_gpu}')
    print()

def calc_uvahalf():
    filename = "l1-uvahalf.log"
    with open(filename, 'r') as r:
        lines = [line for line in r]
        from_host_to_gpu = lines[9:13].copy()
        from_gpu_to_gpu = lines[13:].copy()

    speed_from_host_to_gpu = get_avr([float(res.split()[6]) for res in from_host_to_gpu])
    speed_from_gpu_to_gpu = get_avr([float(res.split()[7]) for res in from_gpu_to_gpu])
    print('Test uvahalf')
    print(f'AVR speef from host to gpu: {speed_from_host_to_gpu}')
    print(f'AVR speef from gpu to gpu: {speed_from_gpu_to_gpu}')
    print()



calc_halfduplex()
calc_uvahalf()
