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



## Storyboard
The figure 4 shows the storyboard for the real estate firm. Each node in the storyboard represents a webpage (screen). The storyboard shows what webpages are navigable from a given webpage.
<img width="965" alt="9" src="https://user-images.githubusercontent.com/34618387/92947965-5033f500-f41e-11ea-99a8-4aa42ae93c7a.png">



## System Component Design for the Real Estate Firm
An Illustration (incomplete)
Introduction
The system (subsystem) internal design for the Real Estate Firm application is presented here. The system internal design shows the internal interactions, i.e., what (software) classes exist in the subsystem component and how do they collaborate to support responsibilities (use cases) documented through the UI objects. The next section shows the use case realizations using the Model-View-Controller pattern. We show the interactions among various classes using a sequence diagram for each use case (system function). We also develop a design class diagram showing the software classes and their interdependencies.
(Please note that this illustration shows the realization of only three use cases.)
Use Case Realization
As shown in the menu bar, the following use cases are available to users. 1. Maintain Property
2. Maintain Owner
3. Maintain Employee
4. Manage Sales Office
5. Maintain Firm.
The menu bar lists the use cases as menu choices. The following use cases are realized:
1. Maintain Owner (referred to as Owner in the menu bar). When clicked on this menu choice, it displays a list of owners. So, it’s equivalent to the use case “List Properties”.
2. Maintain Property (referred to as Property in the menu bar). This is the same as “List Properties.”
3. Manage Sales Office (referred to as Sales Office in the menu bar). This is the same as “List Sales Offices.”
Figures 1, 2, and 3 show the use case realization of Owner and Property and Sale Office respectively. Figure one shows the interaction among four objects—HomePage, OwnerController, OwnerModel and OwnerView. The interaction for other actions on an owner—Edit, Detail, and Delete are not shown.
<img width="753" alt="10" src="https://user-images.githubusercontent.com/34618387/92947963-4f9b5e80-f41e-11ea-85e1-05cc4ad68a17.png">




## Design Class Diagram
Figure 4 shows a deign class diagram that includes software classes and their interdependencies. The software classes and their dependencies are derived directly from the sequence diagrams.
<img width="761" alt="11" src="https://user-images.githubusercontent.com/34618387/92947961-4f02c800-f41e-11ea-9963-2def9181375a.png">





## System Component--Internal Structure
Design subsystems (subcomponents) are used to organize related software classes into groups. We can organize software classes based upon view, functionality, or any other basis that provides a good overall architecture of the system. Here, we will divide our software classes into three subsystems--Views (presentation layer (UI) subsystem), Controllers (business layer control classes), and Models (data access layer and Business logic software classes). These subsystems are described below. Refer to the design class diagram in figure 4 for an overall set of software classes to be organized into components.
### Views
All software classes dealing with UI are grouped together as Views. Based upon the use case realizations, we have the following UI related classes:
1. OwnerView
2. PropertyView
3. SalesOfficeView
All UI related classes will be organized into a single software module.
### Controllers
This subsystem contains software classes needed to implement the coordination between Views and Models. The controller classes are:
1. OwnerController
2. PropertyController
3. SalesOfficeController
All controller related classes will be organized into a single, separate software module.
### Models
This subsystem contains software classes to implement data access and business logic. The model classes are:
1. OwnerModel
2. PropertyModel
3. SalesOfficeModel
All model related classes will be organized into a single, separate software module.
This project doesn’t have any software classes to communicate with a third party system.
## Deployment Model
A deployment model shows the physical nodes (computer hardware) such as client and server machines used to host the various components of an application (software system). The deployment model for the Real Estate Firm application is shown in figure 5. The application is a web-based application. The nodes communicate with each other on the Internet using TCP/IP protocols.




<img width="458" alt="7" src="https://user-images.githubusercontent.com/34618387/92947969-50cc8b80-f41e-11ea-9956-331da7ef206b.png">
<img width="1011" alt="8" src="https://user-images.githubusercontent.com/34618387/92947966-5033f500-f41e-11ea-8774-cd59aad17145.png">


<img width="750" alt="12" src="https://user-images.githubusercontent.com/34618387/92947958-4e6a3180-f41e-11ea-84bb-cae771b3403c.png">
<img width="884" alt="13" src="https://user-images.githubusercontent.com/34618387/92947955-4dd19b00-f41e-11ea-8a9f-26d6c926a3e1.png">
<img width="715" alt="14" src="https://user-images.githubusercontent.com/34618387/92947950-4c07d780-f41e-11ea-8a5f-f38c66bdf39f.png">
