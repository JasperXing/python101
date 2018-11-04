a = [1,4,6,2,5,2,5]

set(a)

def dedupe(items):
    """元素都是hashable"""
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
