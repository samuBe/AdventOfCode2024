def detect_safe(report):
    diff = (report[1] - report[0])
    for level_i in range(1, len(report) - 1):
        if abs(diff) < 1 or abs(diff) > 3:
            return False, level_i + 1
        temp = (report[level_i + 1] - report[level_i])
        if temp * diff < 0:
            return False, level_i + 1
        diff = temp
    safe = not (abs(diff) < 1 or abs(diff) > 3)
    return safe, len(report) - 1


with open('input_day2.txt') as f:
    reports = list()
    for line in f.readlines():
        reports.append(list(map(int, line.rstrip().split(" "))))
    safe_reports = list()
    for report in reports:
        safe, index = detect_safe(report)
        if not safe:
            for i in range(index-2, len(report)):
                new = report[:i] + report[i+1:]
                safe, _ = detect_safe(new)
                if safe:
                    print(i-index)
                    break
        safe_reports.append(safe)
    print(sum(safe_reports))
    print(len(safe_reports))
