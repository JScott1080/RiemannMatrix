# src/python/memory_management.py

from __init__ import load_memories, save_memory, get_memory_db

def retrieve_relevant_memories(persona, keyword):
    memories = load_memories(persona)
    relevant_memories = [mem for mem in memories if keyword.lower() in mem[0].lower() or keyword.lower() in mem[1].lower()]
    return relevant_memories

def clean_old_memories(persona, max_entries=1000):
    conn = get_memory_db(persona)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM memory")
    count = cursor.fetchone()[0]
    if count > max_entries:
        cursor.execute("DELETE FROM memory WHERE rowid IN (SELECT rowid FROM memory ORDER BY rowid LIMIT ?)", (count - max_entries,))
        conn.commit()
    conn.close()

def analyze_memories(persona):
    memories = load_memories(persona)
    keyword_frequency = {}
    for mem in memories:
        words = mem[0].split()
        for word in words:
            keyword_frequency[word] = keyword_frequency.get(word, 0) + 1
    return keyword_frequency

def batch_save_memories(persona, memory_list):
    for user_input, response in memory_list:
        save_memory(persona, user_input, response)

if __name__ == "__main__":
    # Example usage (for illustration purposes)
    persona = 'AMY'
    keyword = 'hello'
    print(f"Memories containing '{keyword}': {retrieve_relevant_memories(persona, keyword)}")
    print(f"Memory analysis: {analyze_memories(persona)}")
    clean_old_memories(persona, max_entries=500)
