import 'package:lost_and_found/service/firebase_methods.dart';
import 'package:lost_and_found/model/lost_items.dart';

class FirebaseRepository {
  FirebaseMethods _firebaseMethods = FirebaseMethods();


  Future<void> addItemToDb(LostItems item) => _firebaseMethods.addItemToDb(item);

  Future<void> updateItemToDb(LostItems item) =>
      _firebaseMethods.updateItemToDb(item);

  Future<void> deleteItemFromDb(LostItems item) =>
      _firebaseMethods.deleteItemFromDb(item);

  Future<LostItems> fetchItemFromDb(LostItems item) =>
      _firebaseMethods.fetchItemFromDb(item);



  Stream<List<LostItems>> getAllLostItems() =>
      _firebaseMethods.getAllLostItems();


}
