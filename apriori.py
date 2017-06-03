from database import fetch_transactions, transaction_iterator, transaction_count
import pdb
import copy
import math
import logging

# frequency count for every item in a set of transactions
def item_counts(transactions):
    counts = {}
    for t in transactions:
        items = t['items']['value'].split(',')
        for item in items:
            current = counts.get(item) or 0
            counts[item] = current + 1
    return counts

# purge patterns that are contained in larger patterns
def purge_patterns(mined, hard_purge = False, priorities=None):
    sorted_mined = sorted(mined, key=lambda x: -len(x))
    max_patterns = []
    purge_count = 0
    for pattern in sorted_mined:
        purge_list = max_patterns
        if hard_purge:
            purge_list = sorted_mined
        if not contains_pattern(purge_list,pattern,priorities):
            max_patterns.append(pattern)
        else:
            purge_count += 1

    logging.info("purged %s patterns", purge_count)

    mined[:] = max_patterns

# inefficient way of tracking whether a pattern was mined before
def contains_pattern(mined,pattern, priorities=None):
    pattern_found = False
    for mined_p in mined:
        prefix_found = True
        index = -1
        for item in pattern:
            found = False
            # use that the patterns are sorted by priority
            while (index + 1) < len(mined_p):
                index += 1
                if mined_p[index] == item:
                    found = True
                    break
            if not found:
                prefix_found = False
                break;
        if prefix_found and (not pattern is mined_p):
            pattern_found = True
            if priorities:
                logging.info('pattern %s mined twice, %s had it', pattern, mined_p)
            break;

    return pattern_found

# runs the apriori algorithm on the given configuration
def apriori(config):
    return []
