import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:lost_and_found/model/lost_items.dart';

class FirebaseMethods {
  static final firestore = FirebaseFirestore.instance;


  Future<void> addItemToDb(LostItems item) async {
    try {
      print("==========Storing New Item===========");
      await firestore
          .collection("Users")
          .doc(item.id)
          .set(item.toMap());
      print("==========Stored New Item===========");
    } catch (e) {
      print(e.toString());
    }
  }

  Future<void> updateItemToDb(LostItems item) async {
    try {
      String path = "LostItems/${item.id}";
      await FirebaseFirestore.instance
          .doc(path)
          .update(item.toMap());
      print("[INFO] DOC UPDATED");
    } catch (e) {
      print(e.toString());
    }
  }

  Future<void> deleteItemFromDb(LostItems item) async {
    try {
      String path = "LostItems/${item.id}";
      await FirebaseFirestore.instance
          .doc(path)
          .delete();
      print("[INFO] DOC Deleted");
    } catch (e) {
      print(e.toString());
    }
  }

  Future<LostItems> fetchItemFromDb(LostItems item) async {
    try {
      String path = "LostItems/${item.id}";
      Map<String, dynamic> data = await FirebaseFirestore.instance
          .doc(path)
          .get().then((value) => value.data());
      return LostItems.fromMap(data);
    } catch (e) {
      print(e.toString());
    }
  }


  Stream<List<LostItems>> getAllLostItems() {
    String path = "LostItems/";
    final reference = FirebaseFirestore.instance.collection(path);
    final snapshots = reference.snapshots();
    return snapshots.map((snapshot) =>
        snapshot.docs.map((doc) => LostItems.fromMap(doc.data())).toList());
  }
}
