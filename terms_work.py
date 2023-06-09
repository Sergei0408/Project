def get_terms_for_table():
    terms = []
    with open("terms.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            term, definition, source = line.split(";")
            terms.append([cnt, term, definition])
            cnt += 1
    return terms


def write_term(new_term, new_definition):
    new_term_line = f"{new_term};{new_definition};user"
    with open("terms.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]
    terms_sorted = old_terms + [new_term_line]
    terms_sorted.sort()
    new_terms = [title] + terms_sorted
    with open("terms.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))

def write_date(time_now):
    new_date_line = f"{time_now};user"
    with open("date.csv", "r", encoding="utf-8") as f:
        existing_date = [l.strip("\n") for l in f.readlines()]
        title = existing_date[0]
        old_date = existing_date[1:]
    date_sorted = old_date + [new_date_line]
    new_date = [title] + date_sorted
    with open("date.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_date))

def get_date_for_table():
    date = []
    with open("date.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            time, source = line.split(";")
            date.append([cnt, time])
            cnt += 1
    return date