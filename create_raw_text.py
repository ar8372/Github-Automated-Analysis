"""
It extracts repos from csv one by one and creates raw text.
"""
# import pandas as pd
# from utils import * 
from modules import * 
from utils import * 

def get_raw_text():
    df1 = pd.read_csv("repo_report.csv")
    df1 = df1[df1.isForked == 0] # consider only those repo which are not forked
    print(df1.head(2))
    print("____________")

    code_complexity = "Code complexity is a multidimensional concept that goes beyond the mere file structure of a project. It encompasses various factors that influence the intricacy of codebases. These factors include algorithmic complexity, such as the presence of nested loops or conditional statements that affect the execution flow and processing time. Additionally, the coupling and cohesion between classes and modules impact complexity. Highly interconnected components with extensive dependencies tend to introduce intricacies. Cyclomatic complexity, a metric based on control flow, evaluates the number of possible execution paths, revealing the intricacy of decision-making processes. Code duplication can also contribute to complexity, as it requires maintenance efforts and increases the chances of inconsistencies. Furthermore, the proper utilization of design patterns and architectural principles can simplify or complicate a project. It's important to consider these factors when assessing code complexity, allowing for a more accurate understanding beyond the surface-level file structure."
    code_complexity1 = """
    Considering these factors helps in accurately assessing code complexity by providing a holistic understanding of the intricacies present within a codebase. While file structure provides an initial glimpse into project organization, it fails to capture the underlying complexities that can exist within individual code units or their interactions. By taking into account algorithmic complexity, one can evaluate the efficiency and performance implications of code. Code units with nested loops or excessive conditional statements may indicate higher algorithmic complexity, resulting in longer execution times or increased resource usage.
    The concepts of coupling and cohesion shed light on the relationships between different components within the codebase. High coupling, where components are heavily interconnected, can introduce complexity as changes in one component may impact others. On the other hand, low cohesion, where a component performs multiple unrelated tasks, can make the code harder to understand and maintain. Assessing coupling and cohesion helps identify potential challenges in code comprehension and maintainability.
    Cyclomatic complexity measures the number of independent paths within a code unit, revealing the intricacy of decision-making processes. Higher cyclomatic complexity suggests more branching and decision points, which can increase the likelihood of errors and hinder code comprehensibility. By considering cyclomatic complexity, one can pinpoint areas of the codebase that may require additional attention or refactoring to reduce complexity.
    Code duplication is another crucial factor. Duplicate code fragments can lead to inconsistencies and increase the maintenance burden. By identifying code duplication, developers can consolidate common logic into reusable functions or refactor the codebase to promote consistency and reduce complexity.
    Lastly, the application of design patterns and architectural principles can significantly influence code complexity. Well-applied design patterns can improve code readability, modularity, and maintainability, while adhering to architectural principles can ensure a clear separation of concerns and scalable system design. Analyzing the presence and usage of these patterns and principles provides insights into the codebase's overall structural complexity and its alignment with best practices.
    By considering these factors collectively, the assessment of code complexity becomes more comprehensive and accurate. It moves beyond a surface-level evaluation based solely on file structure, enabling a deeper understanding of the intricacies present within the codebase. This approach helps prioritize areas that require attention, promotes code quality, and supports efficient maintenance and development processes.
    """
    work = "\nUsing above information we will try to find which is the most complex project.\n"
    intro = f"There are total {df1.shape[0]} projects. Below we will get details about each of these projects one by one: \n"
    all_text = [code_complexity +work + intro]
    for i,row in enumerate(df1.iterrows()):
        repo_title = row[1].title
        repo_isForked = row[1].isForked
        repo_link = row[1].repo_links

        v, t= get_code(repo_link, "", "", [])
        v2 = "Below we will get details about each of these files one by one:"
        all_text.append(f"{i+1}: Project Name : {repo_title}" + "\n" +f"This project contains {len(t)} main files, namely {', '.join(t)}" + "\n"+ v2 + "\n\t" + v)

        
    with open("a.txt", "w", encoding="utf-8") as x:
        x.write("\n".join(all_text))
