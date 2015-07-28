#FACEBOOK PREP
>
**TOP RESOURCE: [GAYLE SLIDES](http://www.slideshare.net/gayle2/cracking-the-facebook-coding-interview)**

## BEHAVIOR QUESTIONS


> 
### BEHAVIOR
	HINT: BE HUMBLE, BE A GREAT TEAMMATE, BE GREAT ENGINEER, BE PASSIONATE, BE KNOWLEDGEABLE, BE CHALLENGEABLE
	- SHOW YOU'RE SMART AND YOU CAN CODE
	
>
### PITCH
	HINT: Memorize your CV: career, studies, accomplishment, hobbies, projects and past work.
>	
	I'M A MECHATRONICS ENGINEER WITH A PHD IN IT&C WITH A DISSERTATION FOCUSED ON AI AND MULTI-ROBOT CONTROL. 
	SINCE GRAD SCHOOL, I'VE BEEN DOING TECH FOR SOCIAL GOOD INCLUDING CIC.MX, A NON-PROFIT AWARDED BY ERIC
	SCHMIDT'S NEW DIGITAL ERA GRANTS, WHICH WERE GIVEN TO THOSE PROMISING SOCIAL CAUSES WITH TECH BASIS. I'VE
	DONE SEVERAL GEOREFERENCING PROJECTS CLOSE TO GOVERNMENT AND CIVIL SOCIETY ORGANIZATIONS, THOSE CONFORM MY 
	STRONGEST BASE IN SQL AND POSTGRESQL DATABASES. THEN I LEFT CIC.MX TO BUILD A STARTUP WITH A COUPLE OF 
	FRIENDS WHERE WE ARE BUILDING AN ALL-ACCESS API AND EASY TO READ DATA VISUALIZATIONS FROM OUR STATE-RUN
	ELECTRICITY PROVIDER. WE'VE SUCCESSFULLY PULLED DATA FROM EVERY USER AND THE SYSTEM IS READY TO SCALE AS
	ENGAGEMENT COMES. IN FACT THIS PROJECT MOTIVATED ME TO BUILD A MATERIAL-DESIGN BOILERPLATE, WHICH IS NOW
	MY BIGGEST AND MOST PROMISING TECH ADVENTURE FOR EMPOWERING STARTUPS, ENTREPRENEURS AND NON-PROFITS DEV
	TEAMS. THIS IS MOST OF MY TIME OUT OF WORK THAT IS STILL RELATED TO TECHNOLOGY, BESIDES, I'VE JUST 
	BECOME A DAD !
>
	* DEEP DIVE INTO DISSERTATION AS A HARD|COOL PROJECT (HASHTABLE & JSON BASED TRANSFERS AND ALLOCATIONS)
	* DEEP DIVE INTO MBOILERPLATE AS A HARD|COOL PROJECT (NOSQL, CLOUD BASED, SCALABLE, EXTENDIBLE, LOW-COST: SHOW 
	  HOW I LOVE TO BUILD STUFF FAST)
	* THINK OF INCLUDING NIGHTS AND WEEKENDS: OPENCITYAPPS.MX, IPAB, EDUCTIVISM, EMULATED CDMA, NETWORK PALS...

>
### PROCESS
	1. GET INTERVIEW OUTFIT DRY CLEANED IF NECESSARY
	2. REHEARSE STORIES FROM THE INTERVIEW PREP GRID
	3. RE-READ 5 ALGORITH APPROACHES
	4. CONTINUE TO PRACTICE UNTIL DAY OF INTERVIEW
	5. REVIEW LIST OF TYPICAL MISTAKES
	6. PRINT 10 COPIES OF MOST-UPDATED RESUME AND PUT THEM INTO FOLDER
	7. AFTER: WRITE THANK YOU NOTE TO RECRUITER
>	
	DRESS CODE: KHAKIS, SLACKS OR NICE JEANS, POLO SHIRT OR DRESS SHIRT.
	
>
### FACEBOOK
	1. BE ENTREPRENEURIAL
	2. ENHANCE A LOT MBOILERPLATE, SHOW HOW I LOVE TO BUILD STUFF FAST.
	3. DEMONSTRATE "NINJA-SKILLS": 
		3.1 HACK TOGETHER ELEGANT AND SCALABLE SOLUTIONS
		3.2 SHOW HOW YOU GET THINGS DONE

>
### SAMPLE QUESTIONS
	1. Tell Me About a Time When You Gave a Presentation to a Group of People Who Disagreed with You
	2. Tell Me About the Biggest Mistake You Made on a Past Project
	3. Tell Me About a Time When You Had to Deal with a Teammate Who Was Underperforming
	4. Tell Me About a Time When You had to Make a Controversial Decision
	5. Tell Me About a Time When You had to Use Emotional Intelligence to Lead
	
	
<hr>

# TECHNICAL QUESTIONS		
**SKIR**: Scope the problem, Key clues and components, Issues, Repairs

**DRIVE**: Lead the process and be open about issues, Do pseudocode before code

**TEAMWORK**: Tweak, be open to feedback

**PRACTICE**: Interview questions, coding on whiteboard, algorithms, design patterns

###	KNOWLEDGE QUESTIONS
	HINT: REVIEW CS FUNDAMENTALS AND KEY CONCEPTS
		
	- Think on how-to SQL indexing, how-to design patterns, how-to webapp2 
	
**CONCEPTS**
<hr style="border-color:green">
* MEMORY (STACK VS HEAP)

	**The Stack**: *global and local scope variables*
	
       What is the stack? 
       It's a special region of your computer's memory that stores temporary 
       variables created by each function (including the main() function). The 
       stack is a "FILO" (first in, last out) data structure, that is managed and 
       optimized by the CPU quite closely. Every time a function declares a new 
       variable, it is "pushed" onto the stack. Then every time a function exits, 
       all of the variables pushed onto the stack by that function, are freed (that 
       is to say, they are deleted). Once a stack variable is freed, that region of 
       memory becomes available for other stack variables.
		
	   The advantage of using the stack to store variables, is that memory is
	   managed for you. You don't have to allocate memory by hand, or free it once 
	   you don't need it any more. What's more, because the CPU organizes stack 
	   memory so efficiently, reading from and writing to stack variables is very 
	   fast.
		
	   To summarize the stack:

			- the stack grows and shrinks as functions push and pop local variables
			- there is no need to manage the memory yourself, variables are 
			  allocated and freed automatically
			- the stack has size limits
			- stack variables only exist while the function that created them, is 
			  running
			  
		Pros and cons:
		
			  very fast access
			  don't have to explicitly de-allocate variables
			  space is managed efficiently by CPU, memory will not become fragmented
			  local variables only
			  limit on stack size (OS-dependent)
			  variables cannot be resized

	**The Heap**: *global scope variables making use of pointers ( * )*
	
		What is the heap? 
		The heap is a region of your computer's memory that is not managed 
		automatically for you, and is not as tightly managed by the CPU. It is a 
		more free-floating region of memory (and is larger). To allocate memory on 
		the heap, you must use malloc() or calloc(), which are built-in C 
		functions. Once you have allocated memory on the heap, you are responsible 
		for using free() to deallocate that memory once you don't need it any more. 
		If you fail to do this, your program will have what is known as a memory 
		leak. That is, memory on the heap will still be set aside (and won't be 
		available to other processes). As we will see in the debugging sectio, 
		there is a tool called valgrind that can help you detect memory leaks.
		
		Unlike the stack, the heap does not have size restrictions on variable size 
		(apart from the obvious physical limitations of your computer). Heap memory 
		is slightly slower to be read from and written to, because one has to use 
		pointers to access memory on the heap.
		
		Unlike the stack, variables created on the heap are accessible by any 
		function, anywhere in your program. Heap variables are essentially global 
		in scope.
		
		Pros and cons:
			variables can be accessed globally
			no limit on memory size
			(relatively) slower access
			no guaranteed efficient use of space, memory may become fragmented over time as blocks of memory are allocated, 
			then freed
			you must manage memory (you're in charge of allocating and freeing variables)
			variables can be resized using realloc()
			
	**Memory management in Python**
		
		Memory management in Python involves a private heap containing all Python objects and data structures. 
		The management of this private heap is ensured internally by the Python memory manager. The Python memory manager 
		has different components which deal with various dynamic storage management aspects, like sharing, segmentation,
		preallocation or caching.
		
		It is important to understand that the management of the Python heap is performed by the interpreter itself and that 
		the user has no control over it, even if she regularly manipulates object pointers to memory blocks inside that 
		heap. The allocation of heap space for Python objects and other internal buffers is performed on demand by the 
		Python memory manager through the Python/C API functions.
		
		locals() & gloabls() built-in functions output a dictionary of all in-memory variables
		
* BIG-O

	<img src="https://raw.githubusercontent.com/chuycepeda/python-ds/master/big-O/big%20o%20growth%20rates.png" style="width:80%; margin-left:10%">
	
	<img src="https://raw.githubusercontent.com/chuycepeda/python-ds/master/big-O/ds%20ops.png" style="width:100%; margin-left:0%">
	
	<img src="https://raw.githubusercontent.com/chuycepeda/python-ds/master/big-O/sorting%20ops.png" style="width:100%; margin-left:0%">
	
	<img src="https://raw.githubusercontent.com/chuycepeda/python-ds/master/big-O/graph%20ops.png" style="width:100%; margin-left:0%">
	
	<img src="https://raw.githubusercontent.com/chuycepeda/python-ds/master/big-O/heap%20ops.png" style="width:100%; margin-left:0%">		

* BIT MANIPULATION

		Implementation:
			 N = int('10000000000',2) 
			 M = int('10011',2) 
			 binary_m = bin(M)  #str in the form '0b10011'
		
		x << y
		Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). 
		This is the same as multiplying x by 2**y.

		x >> y
		Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.

		x & y
		Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.

		x | y
		Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.

		~ x
		Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. 
		This is the same as -x - 1.

		x ^ y
		Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 
		0, and it's the complement of the bit in x if that bit in y is 1.
	
* POWER OF 2
	
		2^7 = 128 
		2^10 = ~1000 (1KB)
		2^20 = ~1000000 (1MB)
		2^30 = ~1000000000 (1GB)
		2^40 = ~1000000000000 (1TB)
* RECURSION AND MEMOIZATION
	

	**Slow recursive**
	
		def fib(n):
    		return n if n < 2 else fib(n-2) + fib(n-1)
    
    **Memoized**
    
    	Memoisation is a technique used in computing to speed up programs. This is accomplished by memorizing the 
    	calculation results of processed input such as the results of function calls. If the same input or a function call 
    	with the same parameters is used, the previously stored results can be used again and unnecessary calculation are 
    	avoided. In many cases a simple array is used for storing the results, but lots of other structures can be used as 
    	well, such as associative arrays, called hashes in Perl or dictionaries in Python.
    
		def memoize(f):
    		memo = {}
    		def helper(x):
        		if x not in memo:            
            		memo[x] = f(x)
        		return memo[x]
    		return helper

		@memoize
		def fib(n):
    		return n if n < 2 else fib(n-2) + fib(n-1)


* OBJECT ORIENTED DESIGN (REAL WORLD OBJECTS)
* MATH AND PROBABILITY
* THREADS AND LOCKS
* DATABASES
* INDEXING
* SHARDING
* TASK QUEUES
* WEBAPP2

**DESIGN PATTERNS**
<hr style="border-color:blue">
* SINGLETON
* FACTORY

		The factory method pattern deals with the problem of creating objects without specifying the exact class of the 
		object to be created. 

		class A(object):
 			def __init__(self):
 			self.a = "Hello"

		class B(object):
 			def __init__(self):
 			self.a = " World"

		myfactory = {
			"greeting" : A, 
			"subject" : B,
		}

		>>> print myfactory["greeting"]().a
		Hello


###	DESIGN AND SCALABILITY [ARCHITECTURE DESIGN SKILLS]
	HINT: WHAT WHOULD YOU DO AT WORK ? BE REAL: GIVE AWAY THE WEBAPP, DATASTORE AND GOOGLE CLOUD SKILLS.
	
	- Know Twitter, Facebook, Google, Amazon, TinyURL design architectures and why's.
	
	FOLLOW-THROUGH
	1. SCOPE THE PROBLEM
		1.1 IDENTIFY ALL POSSIBLE FEATURES AND FUNCTIONALITIES OF THE SYSTEM
	2. STRUCTURE THE ARCHITECTURE
		2.1 USE WHITEBOARD TO DRAW ALL YOUR PIECES: FRONT-END, ROUTES, HANDLERS, AND MODELS
	3. IDENTIFY KEY ISSUES
		3.1 IS YOUR APP WIRTE-HEAVY OR READ-HEAVY ? WHAT DOES THIS MEANS?
		3.2 HAVE YOU DETECTED BOTTLENECKS? 
		3.3 SHOULD WE DISTRIBUTE THE DATABASE?
	4. RESOLVE THE ISSUES
		4.1 THIS IS A GREAT MOMENT TO ASK FOR FEEDBACK

**MUSTS**
<hr style="border-color:green">	
* MODELING
* SCALABILITY
* MEMORY LIMITS|USAGE
* SORTING AND SEARCHING
* GOOGLE DATASTORE AND APPENGINE SCALABILITY
<hr>

###	ALGORITHMS AND PROBLEM SOLVING [CODING SKILLS]

	HINT: SHOW ANALYTICAL SKILLS, KEEP TRYING, COMMUNICATE YOUR THINKING, MAKE TRADEOFFS
	
	- Master Big-O (Complexity), Trees and Graphs, MergeSort, BFS & DFS, Binary Search, Heaps, Recursion
	- Python DS & Modules: List, Set, Dictionary, Itertools, Random, Collections, Heapq, Time; Functional Programming
	
	FOLLOW-THROUGH
	1. LISTEN
		1.1 PATTERN MATCHING: WHAT PROBLEM IS THIS SIMILAR TO ?
		1.2 GET CLUES
	2. EXAMPLE
	3. BRUTE FORCE
	4. OPTIMIZE
		4.1 (B)OTTLENECKS
		4.2 (U)NNECESSARY WORK 
		4.3 (D)UPLICATE WORK
	5. EXPLAIN|WALKTHROUGH
	6. IMPLEMENT|BEAUTIFY CODE: METHODS AND CLASSES
		6.1 CORRECT CODE
		6.2 EFFICIENT: BIG-O PERFORMANCE, METHODS RE-USE
		6.3 SIMPLE AND MODULAR
		6.4 READABLE
		6.5 MAINTAINABLE
		6.6 BALANCED USE OF DATA STRUCTURES
	7. TEST
		7.1 ANALYZE: LOOKS WEIRD ? ERROR HOT SPOTS?
		7.2 TEST CASES: SMALL, EDGE, BIGGER

	
**FIVE ALGORITHM APPROACHES**
<hr style="border-color:green">
1. EXAMPLIFY

	Write out specific examples until finding|deriving a rule of simplification or formula. Think of x equations (examples) and y variables.

2. PATTERN MATCHING

	Think of familiarity and experience with past problems and modify solution in mind to the related problem. Most of the times a clue is found while carefully listening the problem description. Example: Clock angle.

3. SIMPLIFY & GENERALIZE

	This is a multi-step approach useful when constraints are given. First we simplify a constraint such as the amount of data or memory, and solve for this simpler problem. Once we had it, we adapt the earlier solution for the more complex version. Example: Magazine words

4. BASE CASE AND BUILD

	This is a useful approach when you find a clue for recursion. Try first to solve for n=1, then n=1 and n=2, and it's very possible for you to find a recursive approach when solved to n=4. Example: Permutations

5. DATA STRUCTURE BRAINSTORM

	It's hacky and works. Use different data structures as examples and try to apply each one. You'll be surprised of how easy is to find the best data structure for your problem. Example: Median in growing array.


**DATA STRUCTURES**
<hr style="border-color:blue">
* <span style="color: #FF4081">LIST</span>

	*Description:*
	
	   The list type is a container that holds a number of other objects, 
       in a given order. The list type implements the sequence protocol, 
       and also allows you to add and remove objects from the sequence.
	
	*Implementation:*
		
	   l = [1,2,3]
       l = [1,'word',3]
       l[0] = 1	   		
	
	*Operations:*
    
    	.
       
    *Typical use:*
    
       When you need a mixed collection of data all in one place.
       
       When the data needs to be ordered.
       
       When your data requires the ability to be changed or extended. Remember, 
       lists are mutable.
       
       When you don't require data to be indexed by a custom value. Lists are 
       numerically indexed and to retrieve an element, you must know its numeric 
       position in the list.
       
       When you need a stack or a queue. Lists can be easily manipulated by 
       appending/removing elements from the beginning/end of the list.
       
       When your data doesn't have to be unique. For that, you would use sets.
       
    *Problem clues:*
    
    	.
		
	* <span style="color: #FF4081">TUPLE</span>

		*Description:*
	
	   		Tuples support all operations that do not mutate the data structure
	   		(and with the same complexity classes).
	
		*Implementation:*
    
    		.	   		
	
		*Operations:*
    
    		.
		
		*Typical use:*
    
    		.
    		
    	*Problem clues:*
    
    		.
       
	* <span style="color: #FF4081">STACK</span>

		*Description:*	
		
			.	   		
	
		*Implementation:*
    
    		.	   		
	
		*Operations:*
    
    		.
		
		*Typical use:*
    
    		.
    		
    	*Problem clues:*
    
    		.
	* <span style="color: #FF4081">QUEUE</span>

		*Description:*	
		
			.	   		
	
		*Implementation:*
    
    		.	   		
	
		*Operations:*
    
    		.
		
		*Typical use:*
    
    		.
    		
    	*Problem clues:*
    
    		.

* <span style="color: #FFBE46">SET</span>


	*Description:*	
		
		A set is an unordered collection with no duplicate elements. 
      	Basic uses include membership testing and eliminating duplicate entries. 
      	Set objects also support mathematical operations like union, intersection, 
      	difference, and symmetric difference. Sets have many more operations that 
      	are O(1) compared with lists and tuples.
      	
      	Not needing to keep values in a specific order (which lists/tuples require)
      	allows for faster operations.
      	
      	Frozen sets support all operations that do not mutate the data structure 
      	(and with the same complexity classes).	   		
	
	*Implementation:*
    
    	s = set([1,2,3])	   		
	
	*Operations:*
    
    	.
		
	*Typical use:*
    
    	When you need a unique set of data: Sets check the unicity of elements 
    	based on hashes.
      	When your data constantly changes: Sets, just like lists, are mutable.
      	When you need a collection that can be manipulated mathematically: With 
      	sets it's easy to do operations like difference, union, intersection, etc.
      	When you don't need to store nested lists, sets, or dictionaries in a data 
      	structure: Sets don't support unhashable types.

    		
    *Problem clues:*
    
    	.

* <span style="color: #8AC258">DICTIONARY</span>


	*Description:*	
		
		Dictionaries are sometimes found in other languages as “associative 
		memories” or “associative arrays”. Unlike sequences, which are indexed by a 
		range of numbers, dictionaries are indexed by keys, which can be any 
		immutable type; strings and numbers can always be keys. Most dict 
		operations are O(1).
		
		It is best to think of a dictionary as an unordered set of key:value 
		pairs, with the requirement that the keys are unique (within one 
		dictionary). A pair of braces creates an empty dictionary: {}. Placing
		a comma-separated list of key:value pairs within the braces adds initial
		key:value pairs to the dictionary; this is also the way dictionaries are
		written on output.
		
		The main operations on a dictionary are storing a value with some key and 
		extracting the value given the key. It is also possible to delete a
		key:value pair with del. If you store using a key that is already in use, 
		the old value associated with that key is forgotten. It is an error to 
		extract a value using a non-existent key.
		
		The keys() method of a dictionary object returns a list of all the keys 
		used in the dictionary, in arbitrary order (if you want it sorted, just 
		apply the sorted() function to it). To check whether a single key is in the 
		dictionary, use the in keyword. The values() method returns a list of all 
		values used.	   		
	
	*Implementation:*
    
    	d = {'api_key': 'mwkMqTWFnK0LzJHyfkeBGoS2hr2KG7WhHqSGX0SbDJ4', 
    			'container': 'CONTENTSHERE', 'channel': 'CHANNELHERE'}
    	
    	d = dict([('as',1),('king',10)])   		
	
	*Operations:*
    
    	.
		
	*Typical use:*
    
    	When you need a logical association between a key:value pair.
    	When you need fast lookup for your data, based on a custom key.
    	When your data is being constantly modified. Remember, dictionaries are 
    	mutable.
    		
    *Problem clues:*
    
    	.
	* <span style="color: #8AC258">ORDEREDDICT</span>

		*Description:*	
		
			.	   		
	
		*Implementation:*
    
    		.	   		
	
		*Operations:*
    
    		.
		
		*Typical use:*
    
    		.
    		
    	*Problem clues:*
    
    		.
	
	* <span style="color: #8AC258">GRAPH</span>

		*Description:*	
		
			.	   		
	
		*Implementation:*
    
    		.	   		
	
		*Operations:*
    
    		.
		
		*Typical use:*
    
    		.
    		
    	*Problem clues:*
    
    		.

	* <span style="color: #8AC258">BINARY TREE</span>

		*Description:*	
		
			.	   		
	
		*Implementation:*
    
    		.	   		
	
		*Operations:*
    
    		.
		
		*Typical use:*
    
    		.
    		
    	*Problem clues:*
    
    		.

	* <span style="color: #8AC258">TRIE</span>

		*Description:*	
		
			.	   		
	
		*Implementation:*
    
    		.	   		
	
		*Operations:*
    
    		.
		
		*Typical use:*
    
    		.
    		
    	*Problem clues:*
    
    		.
<br>

**PYTHON [TRICKS](http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html), [BUILT-INS](https://docs.python.org/2/library/functions.html) AND USEFUL STANDARD IMPORTS**

<br>
**Enumerate**
		
			Similar to a dictionary, enumerate returns numeric-keyed value pairs as a list of tuples.
		
			>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
			>>> list(enumerate(seasons))
			[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]


			>>> a = ['Hello', 'world', '!']
			>>> for i, x in enumerate(a):
			...     print '{}: {}'.format(i, x)
			...
			0: Hello
			1: world
			2: !
		
		
**Zip**
	
			>>> a = [1, 2, 3]
			>>> b = ['a', 'b', 'c']
			>>> z = zip(a, b)
			>>> z
			[(1, 'a'), (2, 'b'), (3, 'c')]
			>>> zip(*z)
			[(1, 2, 3), ('a', 'b', 'c')]
		
			#grouping
			>>> a = [1, 2, 3, 4, 5, 6]
			>>> group_adjacent = lambda a, k: zip(*([iter(a)] * k))
			>>> group_adjacent(a, 3)
			[(1, 2, 3), (4, 5, 6)]
			>>> group_adjacent(a, 2)
			[(1, 2), (3, 4), (5, 6)]
			>>> group_adjacent(a, 1)
			[(1,), (2,), (3,), (4,), (5,), (6,)]
		
			#inverting dict
			>>> m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
			>>> m.items()
			[('a', 1), ('c', 3), ('b', 2), ('d', 4)]
			>>> dict(zip(m.values(), m.keys()))
			{1: 'a', 2: 'b', 3: 'c', 4: 'd'}






**ALGORITHMS**
<hr style="border-color:red">
* SORT
	* MERGE-SORT
	* QUICK-SORT
* SEARCH
	* BREADTH-FIRST
	* DEPTH-FIRST
	* BINARY 



<hr>
# THE OFFER
	HINT: HANDLE THE POST-INTERVIEW STRESS
	- Think of deadlines and extensions if necessary
	- Handle with care if you think to decline, keep a line of communication open

**AND YOUR REAL SALARY IS...**
<hr style="border-color:blue">
+ OFFER SALARY

	This is your periodical income.
	
+ SIGNING BONUS, RELOCATION AND ONE-TIME PERKS

	When comparing offers, it's wise to amortize this cash over three years (or however long you expect to stay).
	
+ COST OF LIVING DIFFERENCE

	Silicon Valley, for example, is about 20 to 30% more expensive than Seattle.
	
+ ANNUAL BONUS

	This ranges from anywhere from 3% to 30%.
	
+ STOCK OPTIONS AND GRANTS

	Equity compensation can form another big part. Amortize this cash over three years and lump that value into salary.
	
+ PROMOTION PLAN

	This is not money in your pocket, but it can or can't be in your near future in the company.

+ HAPPINESS FACTOR

	Think of the product, the culture, working hours, and if possible meet your Manager and Teammates.
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 