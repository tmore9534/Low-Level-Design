# **Proxy Design Pattern**  

## **Intent**  
- Provide a lightweight version or placeholder to control access to an object.  
- Add additional behavior like caching, logging, security, or lazy initialization.  

## **Problem**  
- A YouTube client directly fetches videos, causing high bandwidth usage.  
- Repeated requests for the same video lead to redundant API calls.  
- No control over access or performance optimizations.  

## **Solution**  
- Introduce a **Proxy** class that acts as an intermediary.  
- The Proxy manages access to the real object and can add optimizations.  
- In the YouTube example, a **caching proxy** stores previously fetched videos.  

## **Key Concepts**  
- **Proxy Interface**: Same as the real subject, ensuring transparency.  
- **Real Subject**: The actual object that performs operations.  
- **Proxy Object**: Controls access, adds additional behavior like caching or security.  

## **Real-World Analogy**  
- A receptionist in an office who screens visitors before allowing access to the CEO.  

## **Structure**  
1. **Proxy Class**  
   - Controls access to the real object.  
   - Implements the same interface as the real subject.  
2. **Real Subject**  
   - The actual object that performs operations.  
3. **Client**  
   - Interacts with the proxy as if it's the real object.  

## **Pseudocode (Caching Proxy for YouTube API)**  
[code](proxy.py)

## Applicability
| Type                 | Purpose                                                     |
| -------------------- | ----------------------------------------------------------- |
| **Virtual Proxy**    | Delay object creation until needed.                         |
| **Protection Proxy** | Restrict access based on permissions.                       |
| **Remote Proxy**     | Represent an object in another machine or network.          |
| **Caching Proxy**    | Store results of expensive operations.                      |
| **Logging Proxy**    | Track method calls for debugging.                           |
| **Smart Proxy**      | Manage additional responsibilities like reference counting. |

## Steps to Implement
1. Create a **common interface** for both the Real Object and Proxy.
2. Implement the **Real Object** with actual logic.
3. Implement a **Proxy** that wraps the Real Object and controls access.
4. Modify the client to use the Proxy instead of the Real Object.

## Pros and Cons
- client code gets decoupled due to common interface and it doesn't has to know in which functionality or class the requests it processing..
- Controls access without modifying the real object.  
- Supports lazy initialization, caching, and security checks.  


❌ Adds complexity and extra layers of abstraction.  
❌ May introduce performance overhead if overused.  
