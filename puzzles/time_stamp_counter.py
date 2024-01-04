def main(start, end, unique_numbers):
    current = start.split()[1]
    goal = end.split()[1]
    h, m, s = current.split(':')
    s, ms = s.split('.')
    
    start_time = [
        {'val': int(h), 'limit': 24}, 
        {'val': int(m), 'limit': 60}, 
        {'val': int(s), 'limit': 60}, 
        {'val': int(ms), 'limit': 1000}
        ]
    
    results = 0
    count = 0
    for c_time in increment_ts(start_time, 0):
        count += 1
        h, m, s, ms = [x['val'] for x in c_time]
        current = f'{h:02}:{m:02}:{s:02}.{ms:03}'
        if len(list(set([h, m, s, ms]))) == unique_numbers:
            results += 1
        
        if count % 1000000 == 0:
            print(f'Current: {current} | Goal:{goal} | Matched {results}/{count}')

        if current == goal:
            break

    print(f'Found {results} timestamps with only {unique_numbers} numbers')
        
def increment_ts(vals, index):
    max_depth = False
    if index + 1 == len(vals):
        max_depth = True
    
    while vals[index]['val'] != vals[index]['limit']:
        if not max_depth:
            i = index + 1
            for vals in increment_ts(vals=vals, index=i):
                yield vals
            vals[index]['val'] += 1
        else:
            vals[index]['val'] += 1
            yield vals
    
    vals[index]['val'] = 0
    yield vals

if __name__ == '__main__':
    main('2024-01-03 08:14:16.146', '2024-01-03 14:37:36.617', 3)