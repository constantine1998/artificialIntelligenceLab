package AOstar;

public class BackTracking {
	
	public static int h1, h2, minValue, minIndex;
	
	public static Node backTracking(Node node) {
		
		while(true) {
			
			if(node.IsOrNode) {
				if(node.mSize >= 3) {
					minValue = node.children.get(0).hValue;
					minIndex = 0;
				
					for(int i = 0; i < node.children.size();i++) {
						if(minValue > node.children.get(i).hValue) {
							minValue = node.children.get(i).hValue;
							minIndex = i;
						}
					}
				
					node.setMarker(minIndex);
				
				
					node.hValue = node.children.get(minIndex).hValue;
					
					if(node.children.get(minIndex).IsSolved) node.IsSolved = true;
				
				}
				if(node.parent == null) break;
				
				node = node.parent;
			}
			else {
				h1 = node.children.get(0).hValue;
				h2 = node.children.get(1).hValue;
				if(h1 >= h2) {
					node.IsMarkerSet = true;
					node.setMarker(0);
				}
				else {
					node.IsMarkerSet = true;
					node.setMarker(1);
				}
				if(node.children.get(0).IsSolved) {
					node.IsMarkerSet = true;
					node.setMarker(1);
				}
				if(node.children.get(1).IsSolved) {
					node.IsMarkerSet = true;
					node.setMarker(0);
				}
				node.hValue = node.children.get(0).hValue + node.children.get(1).hValue + (node.children.get(0).nxm.get(0)*node.children.get(1).nxm.get(0)*node.children.get(1).nxm.get(node.children.get(1).mSize-1));
				
				if(node.children.get(0).IsSolved && node.children.get(1).IsSolved) node.IsSolved = true;
				if(node.parent == null) break;
				
				node = node.parent;
			}
		}
		
		return node;
	}

}
