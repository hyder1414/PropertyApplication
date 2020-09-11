Business Activities of the Real Estate Firm
Here, we identify the business activities of the firm and model the activities in the form of a use case model.
Based upon the description of the firm, the major activities/sub activities are:
1. List properties for sale.
a. Add a new property
b. Update an existing property
c. Display a list of properties
d. Remove an existing property
2. Maintain owners.
a. Add a new owner
b. Update an existing Owner
c. Remove an existing owner
d. Search owner properties
3. Manage sales offices.
a. Add a new sales office
b. Change an existing sales office
c. Remove an existing sales office
d. Monitor sales office
4. Maintain Employees.
a. Add a new employee
b. Update an existing employee
c. Remove an employee
Function Model
We develop a use case model as a function model to show the functions of the firm as a system.
Use Case Model
A use case model is a collection of related use case diagrams that capture the functions of a target firm in a hierarchical form. The firm has two types of workers—Manager and Employees. Employees perform the day to day activities and managers manage the sales office’s operations. Figure 1 shows the overall context of the real estate firm as a system. Managers and employees are modeled as actors that interact
with the firm as a system. The context diagram has a single use case representing the whole system. The context diagram is expanded into the next level (level 0) of the use case diagram (UCD) detailing the functions contained inside the “Operate real Estate Firm” use case at the context level. Figure 2 shows the level 0 use case diagram for the firm. The level 0 UCD, as shown, contains four use cases. The number and type of the actors at level 0 are the same as that on the context diagram. Each level of use case diagrams must be consistent with the other levels. The use cases at level 0 are further detailed (expanded) at level 1. As an illustration, we show the expansion of only two use cases. The two use cases—Maintain Property and
 Figure 1. A Context Use Case Diagram for the Real Estate Firm.

 Figure 2. A Level 0 UCD of the firm.

Maintain Owner have been expanded at level 1. (Note: for your project, you have to expand all of the level 0 use cases). Figure 3 shows the details of Maintain Property at level 1. The level 1 diagram shows the inside details of the “Maintain Property” use case shown at Level 0. Figure 4 shows the details of
 Figure 3. Level 1 Use case diagram--Maintain Property.
 Figure 4. Level 1 Use case Diagram--Maintain Owner

  Figure 5. Level 1 UCD--Manage Sales Office
 Figure 6. Level 1 UCD--Maintain Employee
Maintain Owner at level 1. Figures 5 and 6 show the details of Maintain Sales Office and Maintain Employee use cases.
Data Model
Here we identify the data objects and develop a data model in the form of a class diagram.

Data Objects in the Real Estate Firm
A data object is an “entity”, whether real or abstract, one is interested in maintaining information about in order to operate the business effectively. These data objects relate to each other. For example, an employee manages a sale office. Here, “manages” relationship relates an employee to a sales office. Another relationship “Assigned To” shows which employee works for which sales office. The data objects and relationships have attributes.
The real estate firm has the following data objects mentioned in its description.
1. Real Estate Firm 2. Sales Office
3. PropertyOwner 4. Employee
5. Property
These data objects are defined clearly by specifying their attributes. Figure 7 presents a class diagram showing the classes (data objects), their attributes, and the relationship between the classes.
Cross Validation of Function and Data Models
The class diagram (i.e. a data model) and the use case model (i.e. a function model) must be consistent with each other. In other words, all the data objects identified in a case must have functions to “Use”
 Figure 7. Class Diagram for the firm.

them and all the identified functions in the case must have the data objects needed for the task. A Data Object-Function matrix can be used to evaluate the consistency between a class diagram and a use case model. A matrix is in the form of a table where each row contains a function and each column contains a data object. All data objects should have a function that creates, reads, updates, and deletes it. Table 1 shows a Function Data (also called Entity-Function) matrix for the firm. We use “X” to indicate that a data object is “used” by a function(s).
Table 1. Data Object function Matrix for the Firm
Display a list of properties Add a new property Update an existing property Delete an existing property Display a list of owners Search owner properties Add a new owner Update an existing owner Delete an existing owner Add a New Employee Modify an Existing Employee Remove an Existing Employee List Employees
Add a New Sales Office Update an existing Sales Office Delete an Existing Sales Office Monitor Sales Office
X X X X
X
X X X X X
X
X X X
X
   Data Function
                                                             X X X X
                                   X
X X X X
     Employee Firm Property
PropertyOwner
PropertyOwnership SalesOffice

As we examine the matrix, we see that there are no functions that use the Firm data object. The firm Data object is an important object because it is needed to maintain information about the firm. So, we need to add a new function say, “Maintain Firm”, to use the data about the firm. Thus, the matrix has enabled us to identify a missing function. This requires us to revise our use case model to include a new function as shown in figure 8. (Note that, in this illustration, I have not expanded the Maintain Firm use case. In your project you need to expand all appropriate use cases.)
Non-Functional Requirements of the Firm
A non-functional requirement specifies criteria and constraints that are used to assess the operation of a system. Examples of non-functional requirement are development costs, operational costs, performance, maintainability, usability, scalability, and security, etc. Here we focus on usability, performance, scaling, and security.
Usability
A software system should be easy to understand and use by the users. Usability principles will be followed to make the user-interface friendly and easy to follow.
 Figure 8. The Firm's revised Use Case Diagram at Level 0.

Performance
The performance depends upon response time, throughput. The system will be able to handle online user queries in less than two seconds. It will support up to 100 transactions per second. The system will be designed in such way that the performance will not degrade as the workload on the system increases.
Scaling
Scaling is the ability of a system to scale up as the volume and the number of users increase. The system will be designed to handle thousands of properties and their owners. More specifically, the system will have the capacity to store:
1. One million properties
2. Two million owners
3. Two thousand sales offices, and 4. Ten thousand employees.
The system will be designed to accommodate the future growth of the firm.
Security
The system will be accessed via the Internet. This will require a controlled access to the system. The confidential information about employees, properties, and owners will be protected by requiring potential users to register into the system. Even though the real estate firm doesn’t store very sensitive information, each user will be required to have an ID and password to access the system. Different types of users will have different levels of access permissions. For example, the managers have permissions to access data about all employees, but an employee will have permission to access only his/her own data.
