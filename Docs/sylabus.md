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
        * Basic setups of tools: Editors, command lines, python and pytest.
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
        * Tactics for debugging, and testing functions.
        * Defining interfaces and respecting them.

 3. _Introduction to Data Structures and Algorithms._
      * Understanding arrays (Python Lists.)
        * Tuples and lists.
        * Mutable and immutable data structures.
        * Records and tuples, and Pyhton's NamedTuples.
        * Iteration on sequences, for loops.
      * _A sequential search algorithm and its unit tests._
         * Bisection search on a sorted array.
         * The big-O notation and asymptotic costs of algorithms.
      * The art of debugging
         * Understand your program: the 'bug' is in your head.
         * Logging: observing the values of variables.
         * Using a debugger to interactivelly step through code.
         * Tracing a program execution.
         * Assert the invariants.
      * _The merge sort algorithm and its unit tests_
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
         * Constructing binary trees -- the OOP approach.
         * Recursion, and drawing tree algorithms, with tikz.
         * Search, Insert & delete operations.
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
       * _Ethics and machine learning_.
         * Algorithmic bias and discrimination.
         * Autonomous robots & harm.

 5. _Development Practices._
       * _Development Processes_
         * Traditional Waterfall, and Spiral methodologies.
         * Problems with traditional methodologies.
         * Agile development.
         * DevOps practices.
       * _Agile development and practices._
         * Composition of an Agile team.
         * User stories and cost.
         * Sprints and velocity.
         * Pair programming.
         * Documentation and version control.
         * Continuous integration, TDD, and `Done Done'.
         * Counter-indications for agile.
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
         * Relational databases and SQL -- using Python & sqlite directly.
         * SQL as an example of a declarative (4GL) language.
         * Object relational mappers, and advantages over custom objects.
         * SQLAlchemy in Python.
         * The ACID properties, and the no-SQL movement.
       * _A Pub search application: Data Representations and serialization._ 
         * XML, JSON and binary data (MSGPACK)
         * Using openstreetmap datasets.
         * Visitor pattern and iterative XML parsing.
         * A simple KD-tree implementation, Longitude, Latitude and GIS systems.
         * Introducing interactive graphics with pygame.
         * Plotting an interactive map with pubs as an PNG image: Model-View-Controller concepts.
       * _Demo or die: The MIT Media Lab doctrine._
         * Beautiful engineering: text & typography, design, visualization, interaction.
       * _The open data movement_
         * Open datasets governance and licensing.
         * Sources of open data.
         * Reproducibility of research.
         * Auditability of decision making.
         * Blockchains and Smart contracts.
         * Tensions with privacy.

 7. _Networked Applications._
       * _Basics of client-server applications._
         * Application example: remote chat.
         * Main architectural components: client, server, network.
         * Data packets and layers in network.
         * Capture of sent and received packets with Wireshark.
         * Network-provided services: resilient and efficient Internet-wide communication.
         * Interface between applications and the network layer: IP addresses and ports.
       * _Designing and implementing clients._
         * Remote chat client side code and tests.
         * Malformed input packets and security concerns.
         * Exploiting vulnerabilities and attacks.
         * Attack demonstration using scapy.
         * Solution: input sanitization.
       * _Security in Computer Systems and Networks (mention)._
         * Computer misuse, abuse and cybercrime.
         * Basic concepts of software security and information security.
         * Security policy, threat model, security mechanisms. 
         * Access control, Cryptography and sanitization.
         * Testing for Security: fuzzing, red teams.
         * Professional obligations to produce safe & secure systems.
       * _Power, and saving power (mention)._
         * The new clients and the Internet of Things.
         * Introducing the RaspberryPi Zero W.
         * Understanding power consumption.
         * Sustainability and computing.
       * _Ethical concerns of an inter-connected world._
         * Interoperability and its regulation.
         * The politics of standards.
         * Network privacy: user tracking and mass surveillance.
         * Net neutrality

 8. _Towards Real Systems._
       * _Why systems are needed._
         * Server requirements: performance, scalability and availability.
         * Performance, scalability and stress tests for the remote chat application.
         * Problems with using the remote chat client side code in a server.
         * Understanding performance bottlenecks: I/O, CPU, network (don't give the latter for granted!).
       * _Dealing with I/O bottlenecks._
         * Measuring the impact of blocking I/O.
         * Exploring the solution design space: How to ensure not to block on I/O? 
         * Solution: The `reactor' pattern.
         * The concept of thread and the threading package.
         * Concurrency: benefits, risks and limitations of multi-thread applications.
         * Checking for (latent) errors in a multi-thread application.
       * _Dealing with CPU bottlenecks._
         * Assessing CPU Bottlenecks.
         * Example of the remote chat server having to store messages as encrypted text.
         * Opportunity: most CPUs nowadays are multi-core.
         * Solution:  multi-core.
         * Using the multiprocessing package.
       * _Dealing with CPU Bottlenecks with code binding (mention)_
         * Compilers, linkers and object code libraries.
         * Introducing CFFI.
         * Binding C or Rust code to Python.
       * _Networked Systems (mention)._
         * Server clusters, server farms and data centers.
         * Adding another layer of scalability with an in-network load balancer
         * SSH access to remote machines.
         * Automation & DevOps with Python fabric.
         * Distributing the computation: code and data.
         * Requesting computations, and fetching results.
         * Is that always quicker?

