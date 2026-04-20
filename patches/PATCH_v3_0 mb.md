Ты эксперт по улучшению промтов. Нужно добавить новый раздел в UNIVERSAL PROMPT GENERATOR v3.0 между STEP 3 и STEP 4.

ЗАДАЧА: Создать раздел "STEP 3.5 — ASSOCIATIVE ARTIFACTS" который будет генерировать тонкие, неочевидные ассоциативные элементы.

ТРЕБОВАНИЯ К НОВОМУ РАЗДЕЛУ:

1. **Структура раздела:**
   - 3a. Первичные ассоциации (2-3 прямых связи с темой)
   - 3b. Вторичные ассоциации (ассоциации к ассоциациям, 3-4 элемента)
   - 3c. Символические артефакты (наиболее удаленные, но связанные элементы, 2-3 штуки)
   - 3d. Классификация по типам: ситуативные / контекстные / символичные
   - 3e. Фильтрация по тонкости (убрать очевидные, оставить изощренные)

2. **Алгоритм генерации:**
   - Начать с ENRICHED THEME из Step 2
   - Построить цепочку: тема → культурная отсылка → смежная область → неочевидный артефакт
   - Использовать принципы: историческая связь, лингвистическая игра, визуальная рифма, концептуальная инверсия
   - Избегать: банальные символы, очевидные метафоры, прямые цитаты

3. **Примеры качественных ассоциаций:**
   - НЕ ХОРОШО: Париж → Эйфелева башня
   - ХОРОШО: Париж → кафе → шахматы → клетчатый пол → оптическая иллюзия
   - НЕ ХОРОШО: Детектив → лупа
   - ХОРОШО: Детектив → дедукция → силлогизм → античная логика → мраморные бюсты

4. **Интеграция с существующими шагами:**
   - Артефакты должны передаваться в STEP 4 (scratchpad) как дополнительные семена
   - В STEP 5 они должны интегрироваться как "signature details" 
   - Разные артефакты для разных слотов спектра

5. **Формат вывода нового раздела:**

STEP 3.5 — ASSOCIATIVE ARTIFACTS
3.5a. Primary associations:

* [association 1]: [theme element] → [direct cultural/historical link]
* [association 2]: [theme element] → [direct cultural/historical link]
* [association 3]: [theme element] → [direct cultural/historical link]

3.5b. Secondary associations:

* [secondary 1]: [primary] → [lateral connection] → [unexpected domain]
* [secondary 2]: [primary] → [lateral connection] → [unexpected domain]
* [secondary 3]: [primary] → [lateral connection] → [unexpected domain]
* [secondary 4]: [primary] → [lateral connection] → [unexpected domain]

3.5c. Symbolic artifacts:

* [artifact 1]: [final distilled element + visual description]
* [artifact 2]: [final distilled element + visual description]
* [artifact 3]: [final distilled element + visual description]

3.5d. Classification:

* Situational: [artifacts that modify scene context]
* Contextual: [artifacts that add environmental detail]
* Symbolic: [artifacts that carry deeper meaning]

3.5e. Subtlety filter:
Rejected (too obvious): [list]
Selected (appropriately subtle): [list]
Artifact distribution:

* Slot 1-2: [contextual artifacts]
* Slot 3: [situational artifacts]
* Slot 4-5: [symbolic artifacts]


Найди в промте строку "## STEP 4 — INTERNAL REASONING" и вставь новый раздел STEP 3.5 прямо перед ней.

В STEP 4 добавь в scratchpad после "SELECTED ARCHETYPES" новую секцию:

ARTIFACT INTEGRATION:

* Slot 1: [which artifacts + how integrated]
* Slot 2: [which artifacts + how integrated]
* Slot 3: [which artifacts + how integrated]
* Slot 4: [which artifacts + how integrated]
* Slot 5: [which artifacts + how integrated]


Выведи ПОЛНЫЙ обновленный промт с этими изменениями.