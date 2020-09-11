# In this project we learn how to collect user stories, archetiect & design and built with agile SDLC methodologies.
We describe a prototype implementation of the Real Estate Firm system. We describe the overall implementation plan, the prototype, testing, and user training. We use the use case diagram and the storyboard as a starting point to discuss the implementation plan.
## Business Activities of the Real Estate Firm
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
<img width="590" alt="1" s
<img width="658" alt="2" src="https://user-images.githubusercontent.com/34618387/92947976-51652200-f41e-11ea-93e8-8e8f0cac116c.png">
<img width="429" alt="3" src="https://user-images.githubusercontent.com/34618387/92947975-51652200-f41e-11ea-8cb0-3e934aa1c382.png">
<img width="446" alt="4" src="https://user-images.githubusercontent.com/34618387/92947973-51652200-f41e-11ea-92f3-6f525b955bcf.png">
<img width="803" alt="15" src="https://user-images.githubusercontent.com/34618387/92947943-4a3e1400-f41e-11ea-9149-3ee0e06e9be4.png">

A use case model is a collection of related use case diagrams that capture the functions of a target firm in a hierarchical form. The firm has two types of workers—Manager and Employees. Employees perform the day to day activities and managers manage the sales office’s operations. Figure 1 shows the overall context of the real estate firm as a system. Managers and employees are modeled as actors that interact
with the firm as a system. The context diagram has a single use case representing the whole system. The context diagram is expanded into the next level (level 0) of the use case diagram (UCD) detailing the functions contained inside the “Operate real Estate Firm” use case at the context level. Figure 2 shows the level 0 use case diagram for the firm. The level 0 UCD, as shown, contains four use cases. The number and type of the actors at level 0 are the same as that on the context diagram. Each level of use case diagrams must be consistent with the other levels. The use cases at level 0 are further detailed (expanded) at level 1. As an illustration, we show the expansion of only two use cases. The two use cases—Maintain Property and


## Data Objects in the Real Estate Firm
A data object is an “entity”, whether real or abstract, one is interested in maintaining information about in order to operate the business effectively. These data objects relate to each other. For example, an employee manages a sale office. Here, “manages” relationship relates an employee to a sales office. Another relationship “Assigned To” shows which employee works for which sales office. The data objects and relationships have attributes.
The real estate firm has the following data objects mentioned in its description.
1. Real Estate Firm 
2. Sales Office
3. PropertyOwner 
4. Employee
5. Property
<img width="432" alt="5" src="https://user-images.githubusercontent.com/34618387/92947972-50cc8b80-f41e-11ea-8abf-8a25e0266b86.png">



## Cross Validation of Function and Data Models
The class diagram (i.e. a data model) and the use case model (i.e. a function model) must be consistent with each other. In other words, all the data objects identified in a case must have functions to “Use”
Class Diagram for the firm
<img width="386" alt="6" src="https://user-images.githubusercontent.com/34618387/92947971-50cc8b80-f41e-11ea-9ced-6674a2a932f3.png">
them and all the identified functions in the case must have the data objects needed for the task. A Data Object-Function matrix can be used to evaluate the consistency between a class diagram and a use case model. A matrix is in the form of a table where each row contains a function and each column contains a data object. All data objects should have a function that creates, reads, updates, and deletes it. Table 1 shows a Function Data (also called Entity-Function) matrix for the firm. We use “X” to indicate that a data object is “used” by a function(s).




<img width="458" alt="7" src="https://user-images.githubusercontent.com/34618387/92947969-50cc8b80-f41e-11ea-9956-331da7ef206b.png">
<img width="1011" alt="8" src="https://user-images.githubusercontent.com/34618387/92947966-5033f500-f41e-11ea-8774-cd59aad17145.png">
<img width="965" alt="9" src="https://user-images.githubusercontent.com/34618387/92947965-5033f500-f41e-11ea-99a8-4aa42ae93c7a.png">
<img width="753" alt="10" src="https://user-images.githubusercontent.com/34618387/92947963-4f9b5e80-f41e-11ea-85e1-05cc4ad68a17.png">
<img width="761" alt="11" src="https://user-images.githubusercontent.com/34618387/92947961-4f02c800-f41e-11ea-9963-2def9181375a.png">
<img width="750" alt="12" src="https://user-images.githubusercontent.com/34618387/92947958-4e6a3180-f41e-11ea-84bb-cae771b3403c.png">
<img width="884" alt="13" src="https://user-images.githubusercontent.com/34618387/92947955-4dd19b00-f41e-11ea-8a9f-26d6c926a3e1.png">
<img width="715" alt="14" src="https://user-images.githubusercontent.com/34618387/92947950-4c07d780-f41e-11ea-8a5f-f38c66bdf39f.png">
