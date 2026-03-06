# Блиц: Мой AI-стек

### 1. IDE и AI-плагины
*   **IDE**: **Cursor**. На текущий момент это ультимативный инструмент благодаря глубокой интеграции AI в контекст всего проекта (Composer mode).
*   **Плагины**: Сторонние плагины (вроде Copilot) в Cursor не использую, так как встроенные функции работы с кодобазой эффективнее.

### 2. Модели и задачи
*   **Claude 3.5 Sonnet**: Основная модель для написания логики, сложного рефакторинга и архитектурных решений. Обладает лучшим "программистским" мышлением.
*   **GPT-4o**: Использую для быстрой генерации простых скриптов, обработки текста или когда нужно быстро уточнить документацию по популярным API.
*   **DeepSeek V3/R1**: Для задач, требующих глубокого логического вывода (reasoning) при ограниченном бюджете.

### 3. Использование MCP (Model Context Protocol)
Использую MCP-серверы для расширения возможностей AI:
*   **Google Search / Brave Search**: Чтобы AI мог проверять актуальные версии библиотек (например, последние изменения в API Telegram).
*   **Filesystem**: Для безопасного чтения и анализа структуры больших локальных проектов.
*   **GitHub**: Для автоматизации создания Pull Requests и анализа Issue.

### 4. Системные инструкции и .cursorrules
Да, активно использую `.cursorrules` для поддержания чистоты кода. 
**Самые полезные правила:**
1.  **Strict Typing**: "Always add type hints to Python functions and return types".
2.  **DRY & KISS**: "Before writing new code, check if logic can be reused. Prefer simple solutions over over-engineering".
3.  **Documentation**: "Write docstrings for all public methods explaining 'Why', not just 'What'".
4.  **Error Handling**: "Never use bare 'except:'. Always catch specific exceptions and log them".
