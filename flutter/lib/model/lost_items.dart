class LostItems{
  String id;
  String name;
  String description;
  String dateTime;
  String userName;
  String userNumber;

  LostItems({
    this.id,
    this.name,
    this.description,
    this.dateTime,
    this.userName,
    this.userNumber,
  });

  Map<String, dynamic> toMap() {
    return {
      'id': this.id,
      'name': this.name,
      'description': this.description,
      'dateTime': this.dateTime,
      'userName': this.userNumber,
      'userNumber': this.userNumber,
    };
  }

  factory LostItems.fromMap(Map<String, dynamic> data) {
    return LostItems(
      id: data['id'],
      name: data['name'],
      description: data['description'],
      dateTime: data['dateTime'],
      userName: data['userName'],
      userNumber: data['userNumber'],
    );
  }
}