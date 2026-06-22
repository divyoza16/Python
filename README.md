## Flowchart (auto-generated from the Program Flow data)

```mermaid
flowchart TD
    N0["Welcome and Instructions<br/>- Display a welcome message and a brief description of what the program does."]
    N1["Collect Information<br/>- Prompt the user for name (string), age (int), height (float), favourite number (int)."]
    N2["Data Processing<br/>- Perform calculations with user-provided data, e.g. determine birth year from age.<br/>- Print each variable's value, data type, and memory address via type() and id()."]
    N3["Display Results<br/>- Print a user-friendly summary of the collected information.<br/>- Show messages explaining how data types were converted where applicable."]
    N4["Exit Message<br/>- End with a thank-you message and encourage the user to explore Python further."]
    Start --> N0
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> End([End])# Python
