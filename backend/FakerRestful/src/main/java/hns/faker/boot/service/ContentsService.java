package hns.faker.boot.service;

import hns.faker.boot.dto.ContentsVo;

public interface ContentsService {
	public int insertContents(ContentsVo contents);
	public int updateContents(ContentsVo contents);
	public int deleteContents(int contents_id);
	public ContentsVo selectContents(int contents_id);
}
