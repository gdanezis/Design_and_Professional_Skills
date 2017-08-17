# Syllabus for ENGS102P - Design and Professional Skills

 1. *Meta-Stuff*
      * What is this course about?
      * Schedule
      * Assessment.
      * Integration with IEP.

 2. *Basics of Computer Programming & Software Engineering.*
      * _What is Computer Science and Software Engineering._
        * Programming languages and Python 3 
        * Importance of rapid prototyping.
        * Basic setups of tools: Editors, command lines, pyhton and pytest.
        * Where to find documentation.
        * Interactive python console and executing python programs.
      * _"Hello World" and unit tests._
        * The idea of test Driven Development, its rationale and practice.
        * Names, Assignments, variables and types.
        * Integer types and expressions.
        * What is an Algorithm.
      * _Euclid's GCD algorithm and its unit tests._
        * The notion of refactoring code.
        * Conditionals and While loops in Euclid's algorithm.
        * The notions of conditions and booleans.
        * Euclid from a straight line program to a function.
        * What are functions in programming.
        * Errors and Exceptions in Euclid's algorithms.
        * Integer representations and limits in computers.
      * _The SQRT algorithms and its unit tests._
        * Iterative and approximate algorithms.
        * Floating point representation of real numbers in computers.
        * Testing & conditions floating point algorithms.
      * _Computing logarithms and its unit tests_
        * Approximations and Taylor series.
        * Handling exceptions and understanding modules.
      * _Understanding functions._
        * Passing by reference or value.
        * Pure functions, side effects, declarative programming.

 3. _Introduction to Data Structures and Algorithms._
      * Understanding arrays (Python Lists.)
        * Tuples and lists.
        * Iteration on sequences, for loops.
      * _A sequential search algorithm and its unit tests._
         * Bisection search on a sorted array.
         * The big-O notation and asymptotic costs of algorithms.
      * _The quicksort algorithm and its unit tests_
         * Sorting Algorithms, stable sorting. 
         * Understanding recursion.
         * Divide and conquer strategy.
         * A recursive implementation of quicksort.
         * The asymptotic cost of quicksort.
         * Average-case versus worse case analysis.
      * _Generic programming: Sorting strings and search._
         * What is a string: ASCII and Unicode.
         * Basic methods of strings: what is a method.
         * Adapting quicksort to strings.
       * _Basic I/O and files: Building a simple database._
         * The memory hierarchy.
         * A stream abstraction. A random access abstraction.
         * Modes of opening files. 
         * read() and write(). Formatting of strings.
         * Standard input and output.
         * Blocking I/O.
         * Managing Gigabytes, and scaling systems up.
         * Performance evaluation: micro-benchmarks, profiling, and hot loops.
         * The dangers of early optimization.
       * _Privacy and Databases._
         * The importance of indexes, and social consequences of search.
         * Data versus Personal Data.
         * The problem of deletion and indexes.
         * Data protection frameworks.

 4. _Engineering Dynamic Data Structures._
       * _Linked lists, refactoring and understanding objects_
         * Understanding dynamic structures: insertion, deletion.
         * The "cons" operations on lists.
         * Other operations on lists: search and tail.
         * Patterns of combining data and algorithms: object oriented design.
         * From a function based list implementation, to refactoring to objects.
         * Mutable and immutable data structures.
         * The filter, map and fold functions -- Python shorthands.
         * Packaging, Comments, and documentation.
         * Iterator pattern, and Python generators.
       * _Object Oriented design._
         * Access control, Encapsulation, Reflection
         * Generic programming.
         * Composite pattern.
         * Design Patterns and UML.
       * _Trees and maintaining sorted structures._
         * What are Trees in Computer Science.
         * Tree invariants.
         * Constructing trees.
         * Recursion, and drawing tree algorithms, with latex / tikz.
         * Sorted trees, and insert operation.
         * Search in trees: depth-first, breath-first.
         * Abstract interfaces, and encapsulation.
         * The problem of balancing trees, and advanced tree structures.
       * _Python Dictionary types._
         * Interface to dictionaries.
         * Time complexity of operations.
         * Set and frozenset datatypes.
         * Reference to hash tables.
         * (Cryptography and Cryptanalysis: breaking ciphers.)
       * _Machine Learning: random decision forests._
         * Understanding machine learning.
         * Data and Labels.
         * Example tasks: distinguishing French from Spanish text.
         * Building a decision tree.
         * Building a decision Forrest.
         * Performing classification.
         * Testing and evaluation of machine learning algorithms.
       * (Stacks, Queues, Priority Queues).

 5. _Development Practices._
       * _Development Processes_
         * Traditional Waterfall, and Spiral methodologies.
         * Problems with traditional methodologies.
         * Agile development and practices.
         * DevOps practices.
       * _Building a data science processing pipeline_
         * CSV data.
         * Numpy and numerical libraries.
         * Concurrent development & Refactoring without fear with version control (Git & Github).
         * Using dependency tracking and build tools (make and doit).
         * Integrating all processes into the build.
         * Command line interfaces.
         * Automating all operations & testing.
         * Automating technical drawings with Tikz.
         * Automating technical graphs with pyplot / matplotlib.
         * Data and reproducibility.
       * _Packaging software and Continuous integration._
         * Code review and automated testing.
         * Understanding the process of multi-dev & team 'build'.
         * Working with branches, merging and integrating.
         * End-to-end testing and interface testing.
         * Software repositories and package managers.
         * Standard libraries and third party libraries.
         * Understanding dependencies and modules.
       * _Understanding Intellectual property._
         * Copyright and licensing for software and documents. Trademarks.
         * Patents, software and controversies.
         * DRM and controversies.

 6. _Data and Databases._
       * _`Data belongs to the Database'_
         * Modern database systems.
         * Relational databases and SQL.
         * Object relational mappers, and advantages over own objects.
         * SQLAlchemy in Python.
       * _Graphs and their representations._
         * Matrix and adjacency lists.
         * (Basic Graph algorithms: ...)
         * Routing with the A* algorithm.
         * Dynamic algorithms. Greedy algorithms.
         * A Simple pub database, with comments and ratings.
       * _Representations: XML, JSON and binary data (MSGPACK)_
         * A Pub map application using openstreetmap.
         * Visitor pattern and iterative XML parsing.
         * A simple KD-tree implementation, Longitude, Latitude and GIS systems.
         * Introducing interactive graphics with pygame.
         * Plotting an interactive map with pubs as an PNG image: Model-View-Controller concepts.
       * _Demo or die: The MIT Media Lab doctrine._

 7. _Web Technologies, Security and Usability._
       * _Basics of client Server technologies._
         * HTML, CSS, JS, and all that.
         * Modern back-end architectures: MVC, and micro-services.
         * The Python Flask framework.
       * _Building a web app: Rating Pubs._
         * Testing web applications, with Selenium.
         * Capturing user input.
         * Malformed input and security concerns.
         * Cross side scripting, and insecure inputs.
         * Solution: sanitization. 
       * _Security in Computer Systems._
         * Computer Misuse and Cybercrime.
         * Basic concepts of software security and information security.
         * Professional obligations to produce safe & secure systems.
         * Testing for Security
       * _User interfaces and User Interactions._
         * How can you tell that your system is usable?
         * UX and Design.
         * Techniques to test usability of a system.
         * Accesibility and human dignity in design.

 8. _Concurrency, Correctness and Performance._
 9. XXX


