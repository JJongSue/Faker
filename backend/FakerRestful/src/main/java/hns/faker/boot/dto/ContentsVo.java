package hns.faker.boot.dto;

public class ContentsVo {
	private int contents_id;
	private int user_id;
	private String contents_type;
	private String contents_src;
	public ContentsVo(int contents_id, int user_id, String contents_type, String contents_src) {
		super();
		this.contents_id = contents_id;
		this.user_id = user_id;
		this.contents_type = contents_type;
		this.contents_src = contents_src;
	}
		
	//insert시 user_id하고 type, src만 받고 insert하는 문 
	public ContentsVo(int user_id, String contents_type, String contents_src) {
		super();
		this.user_id = user_id;
		this.contents_type = contents_type;
		this.contents_src = contents_src;
	}

	public int getcontents_id() {
		return contents_id;
	}
	public void setcontents_id(int contents_id) {
		this.contents_id = contents_id;
	}
	public int getUser_id() {
		return user_id;
	}
	public void setUser_id(int user_id) {
		this.user_id = user_id;
	}
	public String getcontents_type() {
		return contents_type;
	}
	public void setcontents_type(String contents_type) {
		this.contents_type = contents_type;
	}
	public String getcontents_src() {
		return contents_src;
	}
	public void setcontents_src(String contents_src) {
		this.contents_src = contents_src;
	}
	@Override
	public String toString() {
		return "ContentVo [contents_id=" + contents_id + ", user_id=" + user_id + ", contents_type=" + contents_type
				+ ", contents_src=" + contents_src + "]";
	}
	
}
