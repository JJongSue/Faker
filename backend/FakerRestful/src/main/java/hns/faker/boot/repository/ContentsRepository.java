package hns.faker.boot.repository;

import hns.faker.boot.dto.ContentsVo;

public interface ContentsRepository {
	public int insertContents(ContentsVo contents);
	public int updateContents(ContentsVo contents);
	public int deleteContents(int content_id);
	public ContentsVo selectContens(int content_id);

}
